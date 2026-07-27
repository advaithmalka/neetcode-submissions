class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = set()
        maxLen = 0
        for num in nums:
            hashMap.add(num)

        for num in nums:
            length = 1
            if num - 1 not in hashMap: # start of seq
                while num + 1 in hashMap:
                    length += 1
                    num += 1
            maxLen = max(length, maxLen)
        


        return maxLen 