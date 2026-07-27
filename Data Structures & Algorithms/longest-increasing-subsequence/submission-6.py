class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        """ [1,4,2,3,2,2,1]
            [9,1,4,2,3,3,7]
               l r
        """
        res = 0
        for l in range(len(nums) - 1, -1, -1):
            for r in range(l + 1, len(nums)):
                if nums[l] < nums[r]:
                    LIS[l] = max(LIS[l], LIS[r] + 1)
            res = max(res, LIS[l])
        return res