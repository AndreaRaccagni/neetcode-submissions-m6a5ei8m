class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def sinkIsland(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            for dr, dc in directions:
                sinkIsland(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    sinkIsland(r, c)

        return islands
