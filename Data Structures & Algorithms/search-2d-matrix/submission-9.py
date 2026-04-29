class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (end - start) // 2 + start
            row = matrix[mid]

            if target > row[-1]:
                start = mid + 1
            elif target < row[0]:
                end = mid - 1
            else:
                return self.binarySearch(row, target)

        return False
   

    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (r - l) // 2 - l

            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True
        
        return False

            