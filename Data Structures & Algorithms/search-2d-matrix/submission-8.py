class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (end + start) // 2

            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                return self.searchRow(matrix[mid], target)

        return False

    def searchRow(self, row, target):
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (r + l) // 2

            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
            else:
                return True

        return False