from config import *
import requests
from bs4 import BeautifulSoup

def read():
    for month in range(1, 13): # months from 1 to 12 (jan-dec)
        url = URLS[month]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        for tr in table.find_all('tr'):
            position, name, club, d, e, f, g, h = [td.string for td in tr.find_all('td')]

