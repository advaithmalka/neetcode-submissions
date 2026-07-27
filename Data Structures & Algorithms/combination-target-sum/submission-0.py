class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, numArr, total):
            if total == target:
                res.append(numArr.copy())
                return
            if total > target or i >= len(nums):
                return

            numArr.append(nums[i])
            dfs(i, numArr, total + nums[i])
            numArr.pop()
            dfs(i + 1, numArr, total)

        dfs(0, [], 0)

        return res