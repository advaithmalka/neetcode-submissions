class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened, closed, subset):
            if opened > n or closed > n or opened - closed < 0: 
                return
            if opened == n and closed == n:
                res.append(subset)
                return
            
            dfs(opened + 1, closed, subset + "(")

            dfs(opened, closed + 1, subset + ")")

        dfs(0, 0, "")
        return res
            
