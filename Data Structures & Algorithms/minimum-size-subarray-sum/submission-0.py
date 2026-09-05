class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        res = len(nums)
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                s -= nums[l]
                res = min(res, r - l + 1)
                l += 1

        return 0 if s < target and r - l + 1 == len(nums) else res
            
