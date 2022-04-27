from bs4 import BeautifulSoup
import requests
from requests.exceptions import InvalidURL
import re
from collections import deque

# funkcja ktora scrapuje wszystkie linki z pierwszej warstwy i zwraca set
def firstLayerScrape(url):
    urls = deque([])
    bad_urls = deque([])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link['href']).startswith('tel:'):
            bad_urls.append(link)
        elif str(link['href']).startswith('mailto:'):
            bad_urls.append(link)
        elif not str(link['href']).startswith('http'):
            link = str(url + link['href'])
            urls.append(link)
        else:
            urls.append(link['href'])
    return set(urls)


# funkcja przyjmuje liste linkow i z regexem szuka adresow mailowych
def extractEmails(list):
    for item in list:
        try:
            emails = deque([])
            r = requests.get(item)
            # trzeba poprawic regex bo u gory wszystko dziala
            email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', r.text)
            if len(email) > 0 :
                for e in email:
                    emails.append(e)
        except InvalidURL:
            print('blad')
            pass
    print(set(emails))
            

extractEmails(firstLayerScrape('http://uszczelki-lubawka.pl'))