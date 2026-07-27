class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = 0
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return strs[0][:r]
            r += 1
        return strs[0][:r]

       