"""
To construc the answer for n data (i.e. P(n)), two secenarios are introduced to simplified
the calculation.

First (one step to the end): The minimal cost of this scenario is S(n-1) + X(n).
Second (two step to the end): The minimal cost of this scenario is S(n-2) + X(n-1).

data = [X(1), X(2), ..., X(n-2), X(n-1), X(n)]
"""


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # temp[]: the cost of length(i)
        n_1 = 0
        n_2 = 0
        temp = None
        penultimate_element = 0
        for element in cost:
            temp = n_1
            n_1 = min(element + n_1, n_2 + penultimate_element)
            n_2 = temp
            penultimate_element = element
        return n_1

if __name__ == "__main__":
    data = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution().minCostClimbingStairs(data)
    print(sol)
