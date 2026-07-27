class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxFreq = 0
        substr = defaultdict(int)
        for r in range(len(s)):
            c = s[r]
            substr[c] += 1
            maxFreq = max(maxFreq, substr[c])
            # invalid
            while (r - l + 1) > maxFreq + k:
                substr[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)

        return res