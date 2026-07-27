class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4,-1,-1,0,1,2

        res = []
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                if r < len(nums) - 1 and nums[r+1] == nums[r]:
                    r-=1
                    continue
                if l > i + 1 and nums[l-1] == nums[l]:
                    l+=1
                    continue

                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return res



        