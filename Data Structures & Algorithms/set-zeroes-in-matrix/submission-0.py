class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        sources = []

        def setRowAndColToZeros(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols:
                return

            matrix[r][c] == 0

            for row in range(0, rows):
                matrix[row][c] = 0

            for col in range(0, cols):
                matrix[r][col] = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    sources.append([r, c])

        for r, c in sources:
            setRowAndColToZeros(r, c)

