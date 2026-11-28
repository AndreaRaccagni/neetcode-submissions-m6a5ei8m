class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        sources = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    sources.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while sources:
            for _ in range(len(sources)):
                r, c = sources.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        sources.append((nr, nc))
            if sources:
                minutes += 1

        return minutes if fresh == 0 else -1