# Solution 1
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
'''
# Solution 2
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  
        self.dfs(candidates, 0, [], target, res)
        return res

    def dfs(self, candidates, start, combination, target, res):
        if target == 0:
            res.append(combination)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target: break
            self.dfs(candidates, i, combination + [candidates[i]], target - candidates[i], res)
'''
