class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in numSet:
                setLen = 1
                while num + 1 in numSet:
                    setLen += 1
                    num += 1
                maxLen = max(maxLen, setLen)

        return maxLen