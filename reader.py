import requests
from bs4 import BeautifulSoup
from config import *

def read(month):

    url = URLS[month]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    players = []
    for tr in table.find_all('tr'):
        attributes = [td.string for td in tr.find_all('td')]
        round_1 = int(attributes[5])
        round_2 = int(attributes[6])
        total = int(attributes[7])
        player = {
            # 'position': attributes[0],
            'name': attributes[1],
            'club': attributes[2],
            'city': attributes[3],
            'category': attributes[4],
            'round_1': round_1,
            'round_2': round_2,
            # 'total': total,
        }

        if round_1 + round_2 != total:
            report('round 1 + round_2 should be equals to total! ({} + {} != {})'.format(round_1, round_2, total))

        players.append(player)

    return players


def report(message):
    print(message)

