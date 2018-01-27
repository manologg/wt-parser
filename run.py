from calculate import calculate_scores


if __name__ == "__main__":
    players = read()
    results = calculate_scores(players)
    sort(results)
    publish(results)
