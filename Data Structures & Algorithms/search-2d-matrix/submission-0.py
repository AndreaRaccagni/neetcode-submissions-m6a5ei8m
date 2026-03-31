class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        top = 0
        bottom = m - 1

        while top <= bottom:
            mid = (bottom - top) // 2 + top

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                return target in matrix[mid]
        return False
