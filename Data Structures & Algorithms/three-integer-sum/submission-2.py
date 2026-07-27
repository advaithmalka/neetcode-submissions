class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num: continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if r < len(nums) - 1 and nums[r+1] == nums[r]: 
                    r -= 1
                    continue
                if l > i + 1 and nums[l-1] == nums[l]: 
                    l += 1
                    continue

                threeSum = num + nums[l] + nums[r]

                if threeSum == 0:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                elif threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                
        return res
                    
                        



