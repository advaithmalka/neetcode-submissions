class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        def midToIndex(mid):
            i = mid // COLS
            j = mid % COLS
            return i, j

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = (l+r) // 2
            row, col = midToIndex(mid)
            value = matrix[row][col]
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return True
        return False
