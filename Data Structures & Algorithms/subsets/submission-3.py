class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subarr = []
        def dfs(i):
            if i == len(nums):
                res.append(subarr.copy())
                return 

            subarr.append(nums[i])
            dfs(i + 1)
            subarr.pop()
            dfs(i + 1)
        
        dfs(0)
        return res