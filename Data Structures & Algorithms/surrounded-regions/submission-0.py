class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        grid = [[False] * cols for _ in range(rows)]

        def overflow(grid, r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == True or board[r][c] == 'X':
                return

            grid[r][c] = True

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                overflow(grid, r + dr, c + dc)

        for c in range(cols):
            overflow(grid, 0, c)
            if rows > 1:
                overflow(grid, rows - 1, c)

        for r in range(1, rows - 1):
            overflow(grid, r, 0)
            if cols > 1:
                overflow(grid, r, cols - 1)
                    
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 'X' if grid[r][c] == False else 'O'



    