class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return s
        maxLen = 0
        res = ""
        for i in range(len(s)):
            l, r = i, i+1 # even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
                
            l, r = i,i # odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res