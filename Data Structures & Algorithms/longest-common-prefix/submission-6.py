class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    idx = i
                    return s[:i]

        return strs[0]