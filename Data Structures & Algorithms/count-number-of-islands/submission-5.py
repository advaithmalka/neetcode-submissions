class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                newRow, newCol = q.popleft()
                if (newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]) or
                    grid[newRow][newCol] != "1"):
                    continue

                grid[newRow][newCol] = "0"
                q.append((newRow + 1, newCol))
                q.append((newRow - 1, newCol))
                q.append((newRow, newCol + 1))
                q.append((newRow, newCol - 1))

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count