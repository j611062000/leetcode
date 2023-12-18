class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n-1)
            cnt, cur, ans = 1, 0, ""
            
            
            while cur < len(prev):
                if cur + 1 < len(prev) and prev[cur] == prev[cur+1]:
                    cnt += 1
                else:
                    ans += str(cnt) + prev[cur]
                    cnt = 1
                cur += 1
                
            return ans

if __name__ == '__main__':
    sol = Solution()
    test_cases = {
        1: "1",
        2: "11",
        3: "21",
        4: "1211",
        5: "111221",
    }
    for i in test_cases:
        print(f"n: {i} ,actual: {sol.countAndSay(i)}, expected: {test_cases[i]}")
        
        