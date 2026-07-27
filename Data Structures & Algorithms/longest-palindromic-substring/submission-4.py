class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+=1
            
            if r - l - 1 > maxLen:
                maxLen = r - l - 1
                res = s[l + 1:r]
            
            # even case
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+=1

            if r - l - 1 > maxLen:
                maxLen = r - l - 1
                res = s[l + 1:r]
        
        return res