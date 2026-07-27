class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(first:bool):
            res = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    res = mid
                    if first:
                        r = mid - 1
                    else:
                        l = mid + 1
            return res
                    

        return [binSearch(True), binSearch(False)]

