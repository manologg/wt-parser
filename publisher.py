from config import *

index_template = open('templates/index').read()
category_template = open('templates/category').read()
player_template = open('templates/player').read()

def ensure_all_fields(player):
    for month in range(1, 13):
        key = 'score_wt_{}'.format(month)
        if key not in player:
            player[key] = ''

    # TODO: should be included ALWAYS
    if 'score_wt_total' not in player:
        player['score_wt_total'] = ''

def publish(total_results):

    categories_html = ''
    for category in CATEGORIES:

        players_html = ''
        players = total_results[category]
        players.sort(key=lambda x: x['score_wt_total'], reverse=True)
        position = 1
        for player in players:
            ensure_all_fields(player)
            player['position'] = '{}.'.format(position)
            players_html += player_template.format(**player)
            position += 1

        categories_html += category_template.format(category=category, players=players_html)

    index_html = index_template.format(categories=categories_html)

    index_file = open('index.html', 'w')
    index_file.write(index_html)
    index_file.close()
