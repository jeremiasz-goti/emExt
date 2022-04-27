from bs4 import BeautifulSoup
import requests
from requests.exceptions import InvalidURL
import re
from collections import deque


def firstLayerScrape(url):
    urls = deque([])
    bad_urls = deque([])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if str(link['href']).startswith('tel:'):
            bad_urls.append
        elif str(link['href']).startswith('mailto:'):
            bad_urls.append
        elif not str(link['href']).startswith('http'):
            link = str(url + link['href'])
            urls.append(link)
        else:
            urls.append(link['href'])
    print(urls)
    return urls

def extractEmails(list):
    for item in list:
        try:
            print(item)
            print('item!')
            r = requests.get(item)
            #regex nie dziala bo znajduje strony pierwszej warstwy ale nie znajduje maila mimo ze mail jest w footerze
            email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.match(email, r.text):
                print('found')
        except InvalidURL:
            print('blad')
            pass
    print(list)
            

extractEmails(firstLayerScrape('https://1stplace.pl'))