class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[len(nums) - 1] = True
        for i in range(len(nums) - 1, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump < len(nums) and dp[i + jump]:
                    dp[i] = True

        print(dp)        
        return dp[0]
