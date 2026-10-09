class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subarr, i):
            if i == len(nums):
                res.append(subarr.copy())
                return 

            subarr.append(nums[i])
            dfs(subarr, i + 1)
            subarr.pop()
            dfs(subarr, i + 1)
        
        dfs([], 0)
        return res