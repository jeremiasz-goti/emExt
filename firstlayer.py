from bs4 import BeautifulSoup
import requests
from requests.exceptions import InvalidURL
import re
from collections import deque


def firstLayer(url):
    urls = deque([])
    bad_urls = deque([])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if not str(link['href']).startswith('http'):
            link = str(url + link['href'])
            urls.append(link)
        elif 'mailto:' or 'tel:' in str(link['href']):
            bad_urls.append
        else:
            urls.append(link['href'])
    return urls

def emExt(list):
    for item in list:
        try:
            print(item)
            # to nie dziala - bo funkcja niby robi item! ale nie znajduje maili a powinna
            print('item!')
            r = requests.get(item)
            email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(email, r.text):
                print('found')
        except InvalidURL:
            print('blad')
            pass

            

emExt(firstLayer('https://1stplace.pl'))