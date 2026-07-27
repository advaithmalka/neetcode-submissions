class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        def binSearch(start):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                k = (l + r) // 2
                if nums[k] < target:
                    l = k + 1
                elif nums[k] > target:
                    r = k - 1
                else:
                    i = k
                    if start:
                        r = k - 1
                    else:
                        l = k + 1
            return i

        return [binSearch(True), binSearch(False)]