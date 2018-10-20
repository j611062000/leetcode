# binary search function
# Input: array, target element, lower bound and upper bound
# Output: the position for insertion
def BS(arr, element, lo, hi):
    while lo <= hi:
        median = (lo + hi) // 2
        pivot = arr[median]
        # We don't take any action if the element is already in the array
        # Thus, we return "N" as an indicator.
        if element == pivot:
            return "N"
        elif element < pivot:
            hi = median - 1
            index = median
        else:
            lo = median + 1
            index = lo
    return index


def lengthOfLIS(nums):
    # Array, M, is used to store the last element for LIS of every length.
    # For insatnce, M[2] stands for the last element of LIS with length of 2
    M = [float("-inf"), ]
    for element in nums:
        insert_position = BS(M, element, 0, len(M) - 1)
        if insert_position != "N":
            # In this case, element is greater than the last element of any LIS.
            if insert_position == len(M):
                M.append(element)

            # In this case, element will replace the LIS with length, insert_position.
            else:
                M[insert_position] = element

    return len(M)-1


print(lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

"""
Function BinarySearch:
    
    Pass In: array, element, lower_bound, upper_bound
    
    While (lower bound <= upper bound):
        
        median = ceiling((lower_bound + upper_bound)/2)
        pivot = array[median]

        if element == pivot:
            It means that there is an value in array as the same as the element
            return "N" 
        
        elif element < pivot:
            hi = median - 1
            index = median
        
        else:
            lo = median + 1
            index = lo
    
    Pass Out: index

EndFunction


Function lengthOfLIS:
    
    Pass In: array of raw data
    
    M <- array used to store the last element of every LIS
    
    For each element in array of raw data:
        insertion_position <- calculated by function, BinarySearch
        
        If insertion_position != "N", then we keep finding which case should we apply

            Case 1: If insertion_position = (the last position of M) + 1
                It means that the element is greater than any other value in M.
                Thus put the element at the tail of the array, M.

            Case 2: If insertion_position != (the last position of M) + 1
                Replace M[insertion_position] with element

    return length of M

End Function
"""