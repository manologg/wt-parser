from reader import read
from calculate import calculate_scores, calculate_total_score
from publisher import publish

if __name__ == "__main__":
    results = dict()
    for month in range(1, 2):  # months from 1 to 12 (jan-dec)
        players = read(month)
        results[month] = calculate_scores(players)

    total_results = calculate_total_score(results)
    publish(total_results, results)
