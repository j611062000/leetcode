class Solution(object):

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        max_record = [arr[0]]
        for element in arr[1:]:
            for count, max_num in enumerate(max_record):
                if element < max_num:
                    temp_max = max_record[-1]
                    if len(max_record) > count:
                        max_record = max_record[:count]
                    max_record.append(max(temp_max, element))
                    break
                elif count == len(max_record)-1:
                    max_record.append(element)
                    break


        return len(max_record)


if __name__ == "__main__":
    data = [5,4,3,2,1]

    print(Solution().maxChunksToSorted(data))
