class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def k2text(k):
            row = k // len(matrix[0])
            col = k % len(matrix[0])
            return row, col
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            k = (l + r) // 2
            row, col = k2text(k)
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: l = k + 1
            else: r = k - 1

        return False