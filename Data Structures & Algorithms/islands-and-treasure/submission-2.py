class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            l = len(q)
            for _ in range(l):
                row, col = q.popleft()
                if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) 
                    or (dist > 0 and grid[row][col] != 2147483647)):
                    continue

                grid[row][col] = dist
                q.append((row + 1, col))
                q.append((row - 1, col))
                q.append((row, col + 1))
                q.append((row, col - 1))
            dist += 1

        