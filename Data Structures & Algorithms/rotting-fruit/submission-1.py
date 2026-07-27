class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = fresh = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = collections.deque()

        # append rotten og to queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
        
        while q and fresh > 0:
            # snapshot of queue
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (len(grid) == row or row < 0 or 
                        len(grid[0]) == col or col < 0 or 
                        grid[row][col] != 1):
                        continue
                
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))

            time += 1

        return time if fresh == 0 else -1
