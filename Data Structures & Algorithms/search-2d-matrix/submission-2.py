class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        T, B = 0, ROWS - 1
        while T <= B:
            row = T + ((B - T) // 2)
            if target > matrix[row][-1]:
                T = row + 1
            elif target < matrix[row][0]:
                B = row - 1
            else:
                break
        if not (T <= B):
            return False
        row = (T + B) // 2
        L, R = 0, COLS - 1
        while L <= R:
            m = L + ((R - L) // 2)
            if target > matrix[row][m]:
                L = m + 1
            elif target < matrix[row][m]:
                R = m - 1
            else:
                return True
        return False
