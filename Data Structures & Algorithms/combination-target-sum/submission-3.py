class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s, arr):
            if s > target or i >= len(nums):
                return 
            
            if s == target:
                res.append(arr.copy())
                return

            arr.append(nums[i])
            dfs(i, s + nums[i], arr)
            arr.pop()
            dfs(i + 1, s, arr)

            
        dfs(0, 0, [])
        return res