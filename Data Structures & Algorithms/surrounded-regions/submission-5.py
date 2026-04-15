class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] == 'X' or (r, c) in visited:
                return

            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for col in range(1, COLS - 1):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = 'X'
                