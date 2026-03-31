class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        return self.hasValidRowsAndCols(board, n) and self.hasValidSquares(board, n)


    def hasValidRowsAndCols(self, grid, n):
        for r in range(n):
            row = set()
            col = set()

            for c in range(n):
                if grid[r][c] in row or grid[c][r] in col:
                    return False
                if grid[r][c] != '.':
                    row.add(grid[r][c])
                if grid[c][r] != '.':
                    col.add(grid[c][r])
        
        return True


    def hasValidSquares(self, grid, n):
        step = int(math.sqrt(n))
        for r in range(0, n, step):
            print(r)
            for c in range(0, n, step):
                square = set()
                for i in range(r, r + step):
                    for j in range(c, c + step):
                        if grid[i][j] in square:
                            return False
                        if grid[i][j] != '.':
                            square.add(grid[i][j])

        return True
