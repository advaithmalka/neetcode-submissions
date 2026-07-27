class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        substr = defaultdict(int)
        maxFreq = 0
        for r in range(len(s)):
            substr[s[r]] += 1
            maxFreq = max(maxFreq, substr[s[r]])
            # invalid
            while (r - l + 1) - maxFreq > k:
                substr[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
