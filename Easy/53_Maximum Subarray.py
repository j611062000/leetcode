class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # g_max(i) = max{g_max(i-1), x(i)+s_max(i-1)}
        # s_max(i) = max{x(i)+s_max(i-1), 0}
        g_max = [0]
        s_max = [0]
        for element in nums:
        	g_max.append(max(g_max[-1], element+s_max[-1]))
        	s_max.append(max(element+s_max[-1], 0))
        return g_max[-1]


