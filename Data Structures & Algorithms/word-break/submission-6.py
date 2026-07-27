class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for l in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) + l <= len(s) and s[l:l + len(word)] == word:
                    dp[l] = dp[l + len(word)]
                if dp[l]:
                    break
        return dp[0]