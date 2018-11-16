for i from 1 to capacity of knapsack:
	for volume from (the first item) to(the last item):

	[4.1]
	# 0/1 knapsack problem with unlimited supply of items
	# dp[i] = True --> a knapsack with volume i can be filled with.
		if dp[i - volume] == True:
			dp[i] == True
		else:
			dp[i] = False
	[4.2]
	# [4.1] and each item has its value
	# dp[i] = integer --> stores the maximum value when the capacity is i
		if dp[i - volume] exists:
        	dp[i] = dp[i - volume] + the "value" corresponds to the current volume

    [4.3] 
    # [4.2] and not restricted to filling the knapsack exactly to capacity
	# dp[i] = integer --> stores the maximum value when the capacity is i
		x = dp[i]
		y = dp[i - item] + the "value" corresponds to the current volume
    	dp[i] = max(x, y)

    	






# if flag = 1, we don't have to fill the knapsack
# Otherwise, we have to fill it.
flag = 0


def unboundedKnapsack(capacity, items):
    dp = {0: 0}
    tracing = {}
    for i in range(capacity + 1):
        for item in items:
            if flag:
                dp[i] = max(dp.get(i, 0), dp.get(i - item, 0) + items[item])
            elif i-item in dp:
                dp[i] = dp[i-item] + items[item]
                # tracing[(dp[i],i)] = (dp[i-item],items[item])


    print(tracing)
    return dp


if __name__ == '__main__':

    # weight / value
    items = {3:1,2:100}

    print(unboundedKnapsack(9, items))
