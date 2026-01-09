from collections import defaultdict


def fruit_into_baskets(fruits):
    start = 0
    # use defaultdict or {}
    state = defaultdict(int)
    max_fruit = 0

    for end in range(len(fruits)):
        # state[fruits[end]] += 1 (also works)
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]  # Important: must delete to reduce len(state) !!!
            start += 1
        max_fruit = max(max_fruit, end - start + 1)
    return max_fruit


fruits = [3, 3, 2, 1, 2, 1, 0]
print(fruit_into_baskets(fruits))
