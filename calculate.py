from config import SCORES


def add_score(players_per_category):
    if len(players_per_category) == 0:
        return players_per_category

    players_per_category.sort(key=lambda x: x['total'], reverse=True)

    players_per_category[0]['score_wt'] = SCORES[0]
    for i in range(1, len(players_per_category)):
        if players_per_category[i]['total'] == players_per_category[i - 1]['total']:
            players_per_category[i]['score_wt'] = players_per_category[i - 1]['score_wt']
        else:
            players_per_category[i]['score_wt'] = SCORES[i]

    return players_per_category


def calculate_scores(players):
    categories = {player['category'] for player in players}

    result = dict()

    for category in categories:
        players_per_category = [player for player in players if player['category'] is category]
        for player in players_per_category:
            player['total'] = int(player['round_1']) + int(player['round_2'])

        players_per_category = add_score(players_per_category)

        result[category] = players_per_category

    return result
