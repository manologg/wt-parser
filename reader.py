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
    
    # Get the first table with more than 2 columns...
    # ... and the first column shall not contain "flight"
    # Yes, it's not that nice

    table = next(t for t in all_tables if len(t) > 2 and 'flight' not in t.find('tr').text.lower())
    
    
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
