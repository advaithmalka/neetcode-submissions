class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        visited = set()
        def dfs(r, c):
            nonlocal res
            if r == m - 1 and c == n - 1:
                res += 1
                return 
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visited:
                return
            
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            visited.remove((r,c))

        dfs(0,0)
        return res