class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        maxCount = count = 0
        for i, letter in enumerate(s):
            if letter in hashMap: 
                count = max(hashMap[letter] + 1, count)
            hashMap[letter] = i
            maxCount = max(maxCount, i - count + 1)
        return maxCount