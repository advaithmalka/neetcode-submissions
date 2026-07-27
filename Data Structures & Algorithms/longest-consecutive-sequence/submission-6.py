class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        numSet = set(nums)

        # find first element
        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                #     numSet.remove(num+length)
                # numSet.remove(num)
                
                count = max(count, length)
        
        return count