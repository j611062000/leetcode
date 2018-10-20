def maxChunksToSorted(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    temp = sorted(arr)
    print(temp)

    flag = 0
    count = 0
    for i in range(len(temp)):
    	if temp[i] == arr[i]:
    		arr[i] = ""

    	if arr[i] != "":
    		flag = 1
    	elif flag == 1:
    		count += 1
    		flag = 0
    print(arr)
    return count

print(maxChunksToSorted([5,4,3,2,1]))
