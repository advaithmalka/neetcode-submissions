class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix[0]) - 1
        bottom, top = len(matrix) - 1, 0
        while l < r:
            for i in range(r - l):

                topLeft = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[bottom - i][top]

                matrix[bottom - i][top] = matrix[bottom][r - i] 

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1
            bottom -= 1
            top += 1