class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        substr = defaultdict(int)
        currLen = 0
        for r in range(len(s)):
            substr[s[r]] += 1
            currLen += 1
            maxFreq = max(substr.values())
            # invalid
            while currLen - maxFreq > k:
                substr[s[l]] -= 1
                currLen -= 1
                if substr[s[l]] == 0:
                    del substr[s[l]]
                l += 1
            res = max(res, currLen)
        return res
