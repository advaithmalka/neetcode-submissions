class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l = 0
        substr = set()
        for char in s:
            while char in substr:
                substr.remove(s[l])
                l += 1
            substr.add(char)
            maxL = max(maxL, len(substr))
        return maxL
            