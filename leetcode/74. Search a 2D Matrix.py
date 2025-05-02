class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1
        if left == right:
            return matrix[0][0] == target
        while left <= right:
            middle = (left + right) // 2
            row = middle // n
            col = middle % n
            element = matrix[row][col]
            if target == element:
                return True
            elif target > element:
                left = middle + 1
            else:
                right = middle - 1

        return False