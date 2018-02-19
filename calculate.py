from config import DATA, SCORES, CATEGORIES


def add_score_to_players(players):
    if len(players) == 0:
        return players

    players.sort(key=lambda x: x['total'], reverse=False)
    players[0]['score_wt'] = SCORES[0]

    for i in range(1, len(players)):
        if players[i]['total'] == players[i - 1]['total']:
            players[i]['score_wt'] = players[i - 1]['score_wt']
        else:
            try:
                next_score = SCORES[i]
            except IndexError:
                next_score = 1
            players[i]['score_wt'] = next_score

    return players


def calculate_scores(players):
    result = dict()

    for category in CATEGORIES:
        players_per_category = get_players_from_category(category, players)
        for player in players_per_category:
            calculate_total_and_key(player)

        players_per_category = add_score_to_players(players_per_category)

        result[category] = players_per_category

    return result

def get_players_from_category(category, players):

    if category == 'D':
        category_check = lambda player_category: player_category in ['D', 'E']
    else:
        category_check = lambda player_category: player_category == category

    return [player for player in players if category_check(player['category'])]

def calculate_total_and_key(player):
    player['total'] = int(player['round_1']) + int(player['round_2'])
    player['key'] = player['name'] # + player['city']

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

    for month in DATA.keys():
        for category in CATEGORIES:
            for player in results[month][category]:
                player_stored = get_player(total_result, player['key'], category)
                if player_stored is None:
                    total_result[category].append({
                        'key': player['key'],
                        'name': player['name'],
                        'club': player['club'],
                        'city': player['city'],
                        'score_wt_' + str(month): player['score_wt']
                    })
                else:
                    player_stored['score_wt_' + str(month)] = player['score_wt']

    calculate_totals(total_result)

    return total_result
