class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s) == 0:
        	return 0
        dp = [1]
        rightmost_num = float("inf")
        for element in s:
        	if rightmost_num >= 3 or element == "0" or int(element) >= 7:
        		dp.append(dp[-1])
        	else:
        		dp.append(dp[-1]+dp[-2])
        	rightmost_num = int(element)
        return(dp[-1])



data = {"00":0,"01":1,"10":2,"11":2,"101":2,"010":2,"001":1,"100":2,"011":2,"110":3}
for test in data:
	print(Solution().numDecodings(test), "ans = {}".format(data[test]))

# global_ans[n] = 1 + local_ans[n-1] +
# 312

# 3 1 2
# 3 12

# 411,23,113,15
# 4 11 23 11 13 15
# C()
