class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subarr):
            s = sum(subarr)
            if i == len(nums) or s > target:
                return
            if s == target:
                res.append(subarr.copy())
                return
            
            subarr.append(nums[i])
            dfs(i, subarr)
            subarr.pop()
            dfs(i + 1, subarr)
        dfs(0, [])
        return res