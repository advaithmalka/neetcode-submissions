class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # presums =    [0, 2, -1, 3, 1, 3, 4, 3]
        # suffuxSums = [5,  8, 4, 6, 4, 3, 4, 0]
        currSum = nums[0]
        res = nums[0]
        for num in nums[1:]:
            if currSum < 0:
                currSum = 0
            currSum += num
            res = max(res, currSum)

        return res