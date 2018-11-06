class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        temp = [0]
        odd = [[1],[2]]
        count = 0
        power = num
        while power>1:
        	power = power/2
        	count+=1
        print(count)

        for i in range(1,num+1):
        	if i%2 == 0:
        		temp.append(temp[-1]+1)
        	else:
        		odd.append([*odd[-1],*[x+1 for x in odd[-1]]])
        print(odd)
        return temp


if __name__ == "__main__":
    data = 9
    sol = Solution().countBits(data)
    print(sol)

# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111
# 10000
# 10001
# 10010
# 10011
# 10100
# 10101
# 10110
# 10111
# 11000
# 11001
# 11010
# 11011
# 11100
# 11101
# 11110
# 11111
# 100000
# 1  3  5 7  9 11...
# 1 /2 /2 3 /2 3 3 4 /2 3 3 4 3 4 4 5 
# 1/2/5/12/28
# for i in range(4):
