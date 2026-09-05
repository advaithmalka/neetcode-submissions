class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxFreq = 0
        numMap = set(nums)

        for num in numMap:
            length = 1
            if num - 1 not in numMap:
                # start of seq
                while num + length in numMap:
                    length += 1
            maxFreq = max(maxFreq, length)

        return maxFreq
