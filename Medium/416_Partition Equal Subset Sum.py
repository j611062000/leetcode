class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums) / 2
            sub_sum = {0}

            for num in nums:
                temp = []
                for element in sub_sum:
                    if num + element == target:
                        return True
                    elif num + element < target:
                        temp.append(num + element)
                sub_sum.update(temp)
            return False


if __name__ == "__main__":
    data = [1, 1, 2]
    sol = Solution().canPartition(data)
    print(sol)

 