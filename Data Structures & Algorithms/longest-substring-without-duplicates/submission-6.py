class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        maxLen = 0
        l = 0
        substrLen = 0
        for letter in s:
            while letter in substr:
                substr.remove(s[l])
                l += 1
                substrLen -= 1
            substr.add(letter)
            substrLen += 1
            maxLen = max(maxLen, substrLen)
        return maxLen
