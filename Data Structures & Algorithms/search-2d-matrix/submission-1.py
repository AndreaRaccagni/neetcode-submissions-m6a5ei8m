class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1

        while top <= bottom:
            mid = (bottom - top) // 2 + top

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

            if top > bottom:
                return False
            
        l, r = 0, n - 1
        row = (bottom - top) // 2 + top
        while l <= r:
            mid = (r - l) // 2 + l

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
            
        return False
