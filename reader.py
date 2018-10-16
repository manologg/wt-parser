import requests
from bs4 import BeautifulSoup
from config import DATA

def read(month):

    data = DATA[month]
    url = data['url']
    parse_function = data['parse_function']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_tables = soup.find_all('table')
    table = all_tables[0] if len(all_tables[0]) > 2 else all_tables[1]
    players = []
    for tr in table.find_all('tr'):
        attributes = [td.string for td in tr.find_all('td')]
        if len(attributes) > 2:
            player = parse_function(attributes)
            if player:
                players.append(player)

    return players

def report(message):
    print(message)
