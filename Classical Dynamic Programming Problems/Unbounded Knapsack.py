def unboundedKnapsack(capacity, items):
    dp = {0: 0}
    for i in range(capacity + 1):
        for item in items:
            if item <= i:
                dp[i] = max(dp.get(i, 0), dp.get(i - item, 0) + items[item])
    return dp


if __name__ == '__main__':

    # weight / value
    items = {5: 10, 10: 30, 15: 20}

    print(unboundedKnapsack(100, items).values())
