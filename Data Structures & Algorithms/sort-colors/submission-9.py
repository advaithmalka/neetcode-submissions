class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while l <= i <= r:
            if nums[i] == 0 and l < i:
                nums[i],nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2 and r > i:
                nums[i],nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i+=1
            