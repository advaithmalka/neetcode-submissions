class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        res = 0
        for i in range(len(nums) - 1, -1, -1):
            lisArray = [1]
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lisArray.append(LIS[j] + 1)

            LIS[i] = max(lisArray)
        return max(LIS)
                