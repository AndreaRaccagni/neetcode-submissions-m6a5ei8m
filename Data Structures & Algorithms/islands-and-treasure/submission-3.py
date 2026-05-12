class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        INF = 2 ** 31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = distance + 1
                        q.append((nr, nc))

            distance += 1