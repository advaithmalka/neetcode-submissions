class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subarr = []

        def dfs(i, s):

            if s == target:
                res.append(subarr.copy())
                return

            if s > target or i == len(candidates):
                return

            

            subarr.append(candidates[i])
            dfs(i + 1, s + candidates[i])
            subarr.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, s)



        dfs(0,0)
        return res