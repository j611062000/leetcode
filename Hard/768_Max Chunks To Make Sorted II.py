import bisect


class Solution(object):

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # max_record = [arr[0]]
        # for element in arr[1:]:
        #     temp_max = max_record[-1]
        #     if element >= temp_max:
        #         max_record.append(element)
        #         continue

        #     max_record = max_record[:bisect.bisect_right(max_record,element)]
        #     max_record.append(temp_max)

        # return len(max_record)
        res,total = 0,0
        for i, j in zip(arr,sorted(arr)):
            total+=i-j
            if not total:
                res+=1
        return res



if __name__ == "__main__":
    data = [2,1,3,4,4,0]

    print(Solution().maxChunksToSorted(data))
