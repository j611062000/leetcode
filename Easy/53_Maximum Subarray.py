class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # g_max(i) = max{g_max(i-1), x(i)+s_max(i-1)}
        # s_max(i) = max{x(i)+s_max(i-1), 0}
        g_max = 0
        s_max = 0
        end = 0
        start = 0
        for element in nums:
            if g_max < element + s_max:
                g_max = element + s_max
                s_max = s_max + element
                end = element
            elif element + s_max > 0:
            	if s_max == 0:
            		start = element
            		s_max = element + s_max
            else:
                s_max = 0
        print(start, end)
        return max(nums) if g_max < 0 else g_max


ans = Solution()
test = [2, -3, 1.5, -1, 3, -2, -3, 3]
print(ans.maxSubArray(test))
