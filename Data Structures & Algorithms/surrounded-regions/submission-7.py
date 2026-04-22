class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        q = deque()

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
                seen.add((r, c))

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc
                
                if 0 <= newRow < rows and 0 <= newCol < cols and (newRow, newCol) not in seen and board[newRow][newCol] == 'O':
                    q.append((newRow, newCol))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in seen:
                    board[r][c] = 'X'