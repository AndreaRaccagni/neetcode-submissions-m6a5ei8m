class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        sources = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    sources.append((r, c))
        
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647

        while sources:
            for _ in range(len(sources)):
                r, c = sources.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        sources.append((nr, nc))
                        grid[nr][nc] = time + 1

            time += 1

