class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return

            board[r][c] = 'V'
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1:
                    dfs(r, c)
                elif c == 0 or c == COLS - 1:
                    dfs(r, c)
                
        for r in range(1, ROWS - 1):
            for c in range(0, COLS, COLS - 1):
                dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                
            
