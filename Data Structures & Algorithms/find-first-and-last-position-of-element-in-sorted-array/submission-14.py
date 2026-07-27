class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binsearch(target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        start = binsearch(target)
        if start >= len(nums) or target != nums[start]:
            return [-1, -1]
        
        return [start, binsearch(target + 1) - 1]