class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        return self.hasValidRowsAndColums(board, n) and self.hasValidSquares(board, n)

    def hasValidRowsAndColums(self, board, n):

        for i in range(n):
            row = set()
            col = set()
            for j in range(n):
                if board[i][j] != '.' and board[i][j] in row:
                    return False

                if board[j][i] != '.' and board[j][i] in col:
                    return False

                row.add(board[i][j])    
                col.add(board[j][i])

        return True

    def hasValidSquares(self, board, n):
        s = int(math.sqrt(n))
        
        for i in range(0, n, s):
            for j in range(0, n, s):
                square = set()

                for k in range(i, i + s):
                    for l in range (j, j + s):
                        if board[k][l] != '.' and board[k][l] in square:
                            return False
                        
                        square.add(board[k][l]) 

        return True
