class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        dp = [False] * len(nums)
        dp[-1] = True
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                dp[i] = True
                goal = i
        return dp[0]
