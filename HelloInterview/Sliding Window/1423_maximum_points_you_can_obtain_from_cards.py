def max_score(cards: list[int], k: int):
    # default sum() function for list[int]
    total = sum(cards)
    if k >= len(cards):
        return total

    state = 0
    min_points = float("inf")
    start = 0

    # we only care about the list of length (len(cards) - k) and find the min
    for end in range(len(cards)):
        state += cards[end]
        # if window length == N - K, then calculate the current min
        if end - start + 1 == len(cards) - k:
            min_points = min(state, min_points)
            state -= cards[start]
            start += 1
    return total - min_points


cards = [2, 11, 4, 5, 3, 9, 2]
print(max_score(cards, 3))

cards = [2, 2, 2]
print(max_score(cards, 2))
