class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subarr = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(subarr.copy())
                return

            

            subarr.append(nums[i])
            dfs(i + 1)
            subarr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res