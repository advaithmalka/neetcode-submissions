class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined = [elem for row in matrix for elem in row]
        
        l, r = 0, len(combined) - 1
        while l <= r:
            k = (l + r) // 2
            if combined[k] == target: return True
            elif combined[k] < target: l = k + 1
            else: r = k - 1

        return False