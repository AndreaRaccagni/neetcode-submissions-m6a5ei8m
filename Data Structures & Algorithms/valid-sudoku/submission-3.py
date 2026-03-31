class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        return self.checkRowsAndCols(board, size) and self.checkSquares(board, size)

    def checkRowsAndCols(self, board, size):
        for i in range(size):
            seenRow = set()
            seenCol = set()
            for j in range(size):
                if (board[i][j] != '.' and board[i][j] in seenRow) or (board[j][i] != '.' and board[j][i] in seenCol):
                    return False
                seenRow.add(board[i][j])
                seenCol.add(board[j][i])
        return True

    def checkSquares(self, board, size):

        def checkSquare(square, size):
            seen = set()
            for i in range(size):
                for j in range(size):
                    if square[i][j] != '.' and square[i][j] in seen:
                        return False
                    seen.add(square[i][j])

            return True

        squareSize = int(math.sqrt(size))

        for i in range(0, size, squareSize):
            for j in range(0, size, squareSize):
                rows = board[i : i + squareSize]
                square = []
                for k in range(squareSize):
                    square.append(rows[k][j : j + squareSize])

                if not checkSquare(square, squareSize):
                    return False

        return True

    