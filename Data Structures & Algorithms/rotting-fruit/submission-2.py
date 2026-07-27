class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        freshFruit = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshFruit += 1

        directions = [[-1,0], [1,0], [0, -1], [0, 1]]
        while q and freshFruit > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if (0 <= newRow < len(grid) and 0 <= newCol < len(grid[0])
                        and grid[newRow][newCol] == 1):
                        grid[newRow][newCol] = 2
                        freshFruit -= 1
                        q.append((newRow, newCol))

        return time if freshFruit == 0 else -1

                    


