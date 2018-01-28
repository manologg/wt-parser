from config import SCORES, CATEGORIES


def add_score(players_per_category):
    if len(players_per_category) == 0:
        return players_per_category

    players_per_category.sort(key=lambda x: x['total'], reverse=False)

    players_per_category[0]['score_wt'] = SCORES[0]
    for i in range(1, len(players_per_category)):
        if players_per_category[i]['total'] == players_per_category[i - 1]['total']:
            players_per_category[i]['score_wt'] = players_per_category[i - 1]['score_wt']
        else:
            players_per_category[i]['score_wt'] = SCORES[i]

    return players_per_category


def calculate_scores(players):
    result = dict()

    for category in CATEGORIES:
        players_per_category = [player for player in players if player['category'] == category]
        for player in players_per_category:
            player['total'] = int(player['round_1']) + int(player['round_2'])
            player['key'] = player['name'] + player['city']

        players_per_category = add_score(players_per_category)

        result[category] = players_per_category

    return result


def get_player(player_list, player_key):
    for player in player_list:
        if player['key'] == player_key:
            return player

    return None


def calculate_total_score(results):
    result = dict()

    for month in range(1, 13):
        for category in CATEGORIES:
            for player in results[month][category]:
                player_stored = get_player(result[category], player['key'])
                if player_stored is not None:
                    result[category].extend(
                        {'key': player['key'], 'name': player['name'], 'score_wt_' + str(month): player['score_wt']})
                else:
                    player_stored['score_wt_' + str(month)] = player['score_wt']
                    result[category][player['key']] = player_stored
    return result
