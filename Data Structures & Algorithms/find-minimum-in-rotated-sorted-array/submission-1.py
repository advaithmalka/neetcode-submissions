class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break

            mid = (l + r) // 2
            
            minVal = min(minVal, nums[mid])
            if nums[l] <= nums[mid]: 
                l = mid + 1 # try to get to right sorted portion of array
            else:  # search to left of right portion
                r = mid - 1
            
        return minVal


            
            

