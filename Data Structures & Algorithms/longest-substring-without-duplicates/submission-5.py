class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        substr = set()
        l = 0
        for char in s:
            while char in substr:
                substr.remove(s[l])
                l += 1
            substr.add(char)
            count = max(count, len(substr))
        return count