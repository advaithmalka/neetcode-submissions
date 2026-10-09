class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subarr = []
        def dfs(i, s):
            if s > target or i == len(nums):
                return
            if s == target:
                res.append(subarr.copy())
                return

            subarr.append(nums[i])
            dfs(i, s + nums[i])
            subarr.pop()
            dfs(i + 1, s)

        dfs(0, 0)
        return res