class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def backtracking(r, c, index):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[index]:
                return False
            
            if index + 1 == len(word):
                return True

            visited.add((r, c))

            for dr, dc in directions:
                if backtracking(r + dr, c + dc, index + 1):
                    return True

            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(r, c, 0):
                    return True
        return False