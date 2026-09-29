class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        sources = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    sources.append((r, c))

        q = deque(sources)
        INF = 2147483647
        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    newRow = r + dr
                    newCol = c + dc
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == INF:
                        q.append((newRow, newCol))
                        grid[newRow][newCol] = count + 1
            
            count += 1

