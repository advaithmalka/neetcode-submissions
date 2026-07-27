class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        sMap = {s[0]:1}
        l = r = 0
        while l <= r and r < len(s):
            substr = s[l:r+1]
            # mostFreq - length <= k
            mostFreq = max(sMap.values())
            if len(substr) - mostFreq <= k:
                res = max(res, r - l + 1)
                r+=1
                if r < len(s):
                    sMap[s[r]] = sMap.get(s[r], 0) + 1
            else:
                sMap[s[l]] -=1
                l+=1

        return res