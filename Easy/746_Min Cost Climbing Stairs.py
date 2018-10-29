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
        n_1 = cost[1]
        n_2 = cost[0]
        temp = None
        for element in cost[2:]:
            temp = n_1
            n_1 = min(n_1, n_2) + element
            n_2 = temp
        return min(n_1, n_2)

if __name__ == "__main__":
    data = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution().minCostClimbingStairs(data)
    print(sol)
