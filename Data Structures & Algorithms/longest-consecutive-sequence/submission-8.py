class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                seq = 0
                while num + seq in numSet:
                    seq+=1
                longest = max(longest, seq)

        return longest