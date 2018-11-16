def unboundedKnapsackOnlyWeight(capacity, items):
    dp = {0: 1}
    combination = {0: [0]}

    for i in range(1, capacity + 1):
        for item in items:
            if item <= i:
                if dp.get(i - item, 0):
                    dp[i] = 1
                    combination[i] = [*combination[i - item], item]
                else:
                    dp[i] = 0

    print(combination)
    return dp


if __name__ == '__main__':

    # weight / value
    items = [2, 3, 5, 6]

    print(unboundedKnapsackOnlyWeight(16, items))
