class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if r < len(nums) - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue 
                    
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return res

               
