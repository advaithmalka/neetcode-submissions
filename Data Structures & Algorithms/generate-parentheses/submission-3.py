class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, opened, closed):
            if opened + closed == 2 * n:
                res.append(s)
                return
            if opened < n:
                dfs(s + "(", opened + 1, closed)
            if closed < n and closed < opened:
                dfs(s + ")", opened, closed + 1)

        dfs("(", 1, 0)
        return res