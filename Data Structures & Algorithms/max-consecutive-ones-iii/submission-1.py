class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = tempRes = 0 
        l = 0
        numZeros = 0
        for r in range(len(nums)):
            if nums[r] == 1 and numZeros <= k:
                res = max(res, r - l + 1)
            else:
                numZeros += 1
                # invalid
                while numZeros > k:
                    if nums[l] == 0:
                        numZeros -= 1 
                    l+=1 
            res = max(res, r - l + 1)
        return res
                    