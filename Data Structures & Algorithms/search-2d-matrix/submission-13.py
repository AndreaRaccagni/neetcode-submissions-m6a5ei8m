class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            row = l + (r - l) // 2

            if target < matrix[row][0]:
                r -= 1
            elif target > matrix[row][-1]:
                l += 1
            else:
                return self.binarySearch(matrix[row], target)
        return False


    def binarySearch(self, row: List[int], target: int) -> bool:
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                l += 1
            else:
                r -= 1
        return False