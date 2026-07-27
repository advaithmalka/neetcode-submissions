class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        for i in range(3):
            for j in range(p1, len(nums)):
                if nums[j] == i:
                    nums[p1], nums[j] = nums[j], nums[p1]
                    p1 += 1