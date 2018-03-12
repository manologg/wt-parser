def parse_8_cols(attributes):

    category = attributes[4]
    if category not in ['A', 'B', 'C', 'D', 'E']:
        print('Category "{}" does not exist --> Ignoring row "{}"'.format(category, ', '.join(attributes)))
        return None

    round_1 = int(attributes[5])
    round_2 = int(attributes[6])
    total = int(attributes[7])
    player = {
        # 'position': attributes[0],
        'name': attributes[1],
        'club': attributes[2],
        'city': attributes[3],
        'category': category,
        'round_1': round_1,
        'round_2': round_2,
        # 'total': total,
    }
    if round_1 + round_2 != total:
        report('round 1 + round_2 should be equals to total! ({} + {} != {})'.format(round_1, round_2, total))

    return player

def parse_9_cols(attributes):
    # 'general_position': attributes[0],
    return parse_8_cols(attributes[1:])

def parse_10_cols(attributes):
    # 'points': attributes[-1],
    return parse_9_cols(attributes[:-1])

DATA = {
    1: {
        'url': "http://www.frisbee-nrw.de/2018/01/13/dziuba-rockt-den-kletterpark/",
        'parse_function': parse_8_cols
    },
    2: {
        'url': "http://www.frisbee-nrw.de/2018/02/10/wt1802-drei-heimsiege-fuer-die-lakers/",
        'parse_function': parse_9_cols
    },
    3: {
        'url': "http://www.frisbee-nrw.de/2018/03/10/wt1803-ergebnisse/",
        'parse_function': parse_10_cols
    },
    #3: {
    #    'url': "",
    #    'parse_function': parse_9_rows
    #},
}

SCORES = [30, 26, 23, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

CATEGORIES = ['A', 'B', 'C', 'D']
