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


def get_player(total_result, player_key, category):
    try:

        for player in total_result[category]:
            if player['key'] == player_key:
                return player
    except KeyError:
        return None

    return None


def get_best_results(player):
    results = {}

    for key in player.keys():
        if key.startswith('score_wt_'):
            results[key] = player[key]

    result_pairs = list(results.items())
    result_pairs.sort(key=lambda x: x[1], reverse=False)
    return [x[0] for x in result_pairs][:7]


def calculate_totals(total_result):
    for category in CATEGORIES:
        for player in total_result[category]:
            best_results = get_best_results(player)

            score_wt_total = 0
            for key in player.keys():
                if key.startswith('score_wt_'):
                    if key not in best_results:
                        player[key] = '[' + str(player[key]) + ']'
                    else:
                        score_wt_total += player[key]

            player['score_wt_total'] = score_wt_total



def calculate_total_score(results):
    total_result = {key: [] for key in CATEGORIES}

    for month in range(1, 13):
        for category in CATEGORIES:
            try:
                for player in results[month][category]:
                    player_stored = get_player(total_result, player['key'], category)
                    if player_stored is None:
                        total_result[category].append(
                            {'key': player['key'], 'name': player['name'],
                             'score_wt_' + str(month): player['score_wt']})
                    else:
                        player_stored['score_wt_' + str(month)] = player['score_wt']
            except KeyError:
                pass  # there is no results for this month

    calculate_totals(total_result)

    return total_result
