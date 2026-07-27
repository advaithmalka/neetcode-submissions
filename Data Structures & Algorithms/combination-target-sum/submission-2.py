class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s, subarr):
            if i == len(nums) or s > target:
                return
            if s == target:
                res.append(subarr.copy())
                return
            
            subarr.append(nums[i])
            dfs(i, s + nums[i], subarr)
            subarr.pop()
            dfs(i + 1, s, subarr)
        dfs(0, 0, [])
        return res