class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = collections.deque()
        def bfs(i,j):
            grid[i][j] = "0"
            queue.append((i+1,j))
            queue.append((i-1,j))
            queue.append((i,j+1))
            queue.append((i,j-1))

            while queue:
                r,c = queue.popleft()
                if  r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0":
                    continue 
                grid[r][c] = "0"
                queue.append((r+1,c))
                queue.append((r-1,c))
                queue.append((r,c+1))
                queue.append((r,c-1))
                

                
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i,j)

        return count