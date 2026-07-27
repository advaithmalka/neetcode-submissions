class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if (row < 0 or col < 0 
                or row >= len(board) or col >= len(board[0]) 
                or board[row][col] == "#" or i >= len(word)
                or board[row][col] != word[i]): 
                return False
            
            if i == len(word) - 1 and  board[row][col] == word[i]:
                return True
            board[row][col] = "#"
            res = (dfs(row + 1, col, i+1) or 
                   dfs(row - 1, col, i+1) or
                   dfs(row, col + 1, i+1) or
                   dfs(row, col - 1, i+1))
            board[row][col] = word[i]
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0): return True

        return False

                
