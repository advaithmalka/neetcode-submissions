class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        subStr = set()
        l, r = 0, 1
        for letter in s:
            if letter not in subStr:
                subStr.add(letter)
            else:
                while letter in subStr:
                    subStr.remove(s[l])
                    l+=1
                subStr.add(letter)
                
            maxLen = max(maxLen, len(subStr))
        return maxLen



