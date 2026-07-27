class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            potentialNum = target - num
            if potentialNum in seen:
                return [seen[potentialNum], i]
            seen[num] = i
