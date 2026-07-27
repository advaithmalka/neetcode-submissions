class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0])):
                return False
            if board[r][c] == "X" or board[r][c] == "#":
                return True

            board[r][c] = "#"
            surrounded = (dfs(r + 1, c) 
                            and dfs(r - 1,c) 
                            and dfs(r, c + 1) 
                            and dfs(r,c - 1))
            board[r][c] = "O"
            return surrounded
                
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    if dfs(r,c):
                        board[r][c] = "X"