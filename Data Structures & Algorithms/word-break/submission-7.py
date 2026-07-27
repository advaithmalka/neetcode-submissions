class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        """
        [f f f f f f f f t]
        [n e e t c o d e]
                     i j
        """
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr in wordDict:
                    dp[i] = dp[j]
                if dp[i]:
                    break
        return dp[0]