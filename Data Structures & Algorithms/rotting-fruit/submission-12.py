class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        sources = deque()
        fresh = 0
        time = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    sources.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while sources:
            for _ in range(len(sources)):
                r, c = sources.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        sources.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2
            if sources:
                time += 1

        return time if fresh == 0 else -1