class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        while l <= r:
            k = (l + r) // 2
            if nums[k] < target:
                l = k + 1
            elif nums[k] > target:
                r = k - 1
            else:
                i = j = k
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                res = [i + 1, j - 1]
                break

        return res