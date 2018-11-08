def knapsackOnlyWeight(capacity, items):
	# dp[(i,j)] = 1 --> consider first i items, capacity j can be filled with.
	dp = {}
	for i in range(-1,len(items)):
		dp[(i,0)] = 1
	for i in range(capacity+1):
		dp[(-1,i)] = 0

	for i in range(len(items)):
		for j in range(1,capacity+1):
			if j>=items[i]:
				dp[(i,j)] = dp[(i-1, j)] or dp[(i-1, j-items[i])]
	temp = []

	for element in dp:
		if dp[element]:
			temp.append(element)
	temp.sort(key = lambda x: x[0])
	print(temp)



if __name__ == '__main__':

    # weight
    items = [2,3,5,6]
    capacity = 16

    print(knapsackOnlyWeight(capacity,items))
