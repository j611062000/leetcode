from typing import List
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        def dfs(idx: int, path: List[int], cur: int):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(i, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res

# print(combinationSum([2,3,6,7], 7))

