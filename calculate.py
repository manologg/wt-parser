def add_score(players_per_category):
    players_per_category = sorted(players_per_category['total'])

    

    return players_per_category


def calculate_scores(players):
    categories = {player['category'] for player in players}

    result = dict()

    for category in categories:
        players_per_category = [player for player in players if player['category'] is category]
        for player in players_per_category:
            player['total'] = player['round_1'] + player['round_2']

        players_per_category = add_score(players_per_category)

        result[category] = players_per_category

    return result


players = [
    {
        'category': 'a',
        'score_wt': 0,
        'round_1': 30,
        'round_2': 40
    }, {
        'category': 'a',
        'score_wt': 0,
        'round_1': 20,
        'round_2': 30
    }, {
        'category': 'a',
        'score_wt': 0,
        'round_1': 30,
        'round_2': 60
    },
]

print calculate_scores(players)
