class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        currLen = 0
        l = 0
        maxF = 0
        substr = defaultdict(int)
        for r in range(len(s)):
            substr[s[r]] += 1
            currLen += 1
            maxF = max(maxF, substr[s[r]])
            while currLen > maxF + k:
                substr[s[l]] -= 1
                l += 1
                currLen -= 1
            maxLen = max(maxLen, currLen)
        return maxLen