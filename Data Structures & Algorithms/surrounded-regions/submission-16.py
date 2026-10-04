class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            if board[r][0] == 'O' or board[r][COLS - 1] == 'O':
                self.dfs(r, 0, ROWS, COLS, board)
                self.dfs(r, COLS - 1, ROWS, COLS, board)

        for c in range(COLS):
            if board[0][c] == 'O' or board[ROWS - 1][c] == 'O':
                self.dfs(0, c, ROWS, COLS, board)
                self.dfs(ROWS - 1, c, ROWS, COLS, board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'C':
                    board[r][c] = 'O'


    def dfs(self, r, c, m, n, board):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        if min(r, c) < 0 or r >= m or c >= n or board[r][c] != 'O':
            return

        board[r][c] = 'C'
        
        for dr, dc in directions:
            self.dfs(r + dr, c + dc, m, n, board)