class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            L, R = 0, len(matrix[row]) - 1
            while L <= R:
                column = L + ((R - L) // 2)
                if matrix[row][column] > target:
                    R = column - 1
                elif matrix[row][column] < target:
                    L = column + 1
                else:
                    return True
        return False