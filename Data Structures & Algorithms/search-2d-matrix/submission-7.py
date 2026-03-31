class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            row = (start + end) // 2
            if target > matrix[row][-1]:
                start = row + 1
            elif target < matrix[row][0]:
                end = row - 1
            else:
                return self.searchRow(matrix[row], target)
        return False
           
    def searchRow(self, row: List[int], target: int) -> bool:
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True
        
        return False