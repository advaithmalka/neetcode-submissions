class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        subboxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".": 
                    continue

                if num in cols[c] or num in rows[r] or num in subboxes[(r // 3, c // 3)]:
                    return False
                cols[c].add(num)
                rows[r].add(num)
                subboxes[(r // 3, c // 3)].add(num)

        return True