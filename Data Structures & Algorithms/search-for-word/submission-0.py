class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def backtracking(r, c, index, visited):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[index]:
                return False

            if index + 1 == len(word):
                return True
            
            visited.add((r, c))

            for dr, dc in directions:
                if backtracking(r + dr, c + dc, index + 1, visited):
                    return True
                
            visited.remove((r, c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and backtracking(r, c, 0, set()):
                    return True

        return False