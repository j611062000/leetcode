from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted(candidates)
        
        def dfs(start, target, path):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
            else:
                for i in range(start, len(candidates)):
                    dfs(i, target - candidates[i], path + [candidates[i]])
        
        dfs(0, target, [])
        return res
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
        