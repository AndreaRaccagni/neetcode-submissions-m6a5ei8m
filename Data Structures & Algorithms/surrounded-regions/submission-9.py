class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        q = deque()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][cols - 1] == 'O':
                q.append((r, cols - 1))

        for c in range(1, cols - 1):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[rows - 1][c] == 'O':
                q.append((rows - 1, c))

        while q:
            r, c = q.popleft()

            if board[r][c] == 'O':
                board[r][c] = 'C'

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'C':
                    board[r][c] = 'O'