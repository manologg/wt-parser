from calculate import calculate_scores
from reader import read

if __name__ == "__main__":
    players = read()
    results = calculate_scores(players)
    sort(results)
    publish(results)
