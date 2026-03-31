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
        squareSize = int(size ** 0.5)

        for row in range(0, size, squareSize):
            for col in range(0, size, squareSize):
                seen = set()
                for i in range(squareSize):
                    for j in range(squareSize):
                        val = board[row + i][col + j]
                        if val != '.' and val in seen:
                            return False
                        seen.add(val)
        return True
        