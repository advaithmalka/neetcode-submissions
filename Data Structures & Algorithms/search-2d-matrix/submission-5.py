class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matLen = len(matrix) * len(matrix[0])
        l,r = 0, matLen - 1
        
        def midToPos(mid):
            return mid // len(matrix[0]), mid % len(matrix[0])

        while l <= r:
            mid = (l + r) // 2
            row, col = midToPos(mid)
            val = matrix[row][col]

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False
