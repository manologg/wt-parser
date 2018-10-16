from __future__ import unicode_literals
from reader import read
from calculate import calculate_scores, calculate_total_score
from publisher import publish
from config import DATA

if __name__ == "__main__":
    results = dict()
    for month in DATA.keys():
        players = read(month)
        results[month] = calculate_scores(players)

    total_results = calculate_total_score(results)
    publish(total_results)
