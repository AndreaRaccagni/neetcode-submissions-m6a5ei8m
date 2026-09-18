class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        return self.isValidRowsAndCols(board, n) and self.isValidSquare(board, n)


    def isValidRowsAndCols(self, board, n):
        for r in range(n):
            row = set()
            col = set()

            for c in range(n):
                if board[r][c] != '.':
                    if board[r][c] in row:
                        return False
                    row.add(board[r][c])
 
                if board[c][r] != '.':
                    if board[c][r] in col:
                        return False
                    col.add(board[c][r])
        return True


    def isValidSquare(self, board, n):
        jump = int(math.sqrt(n))

        for r in range(0, n, jump):
            for c in range(0, n, jump):
                square = set()
                for i in range(r, r + jump):
                    for j in range(c, c + jump):
                        if board[i][j] != '.':
                            if board[i][j] in square:
                                return False
                            square.add(board[i][j])
        return True