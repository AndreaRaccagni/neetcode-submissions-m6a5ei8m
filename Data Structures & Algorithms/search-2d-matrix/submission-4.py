class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1

        while top <= bottom:
            row_index = (bottom - top) // 2 + top
            row = matrix[row_index]

            if row[0] <= target <= row[n - 1]:
                return self.searchRow(row, target)
            if target < row[0]:
                bottom = row_index - 1
            if target > row[n - 1]:
                top = row_index + 1
        
        return False

    def searchRow(self, row: List[int], target) -> bool:
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid -1
            else:
                return True
            
        return False