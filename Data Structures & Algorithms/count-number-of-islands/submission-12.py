class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    self.sinkIsland(r, c, ROWS, COLS, grid)

        return islands
        
    def sinkIsland(self, r, c, m, n, grid):
        if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == '0':
            return

        grid[r][c] = '0'

        self.sinkIsland(r + 1, c, m, n, grid)
        self.sinkIsland(r, c + 1, m, n, grid)
        self.sinkIsland(r - 1, c, m, n, grid)
        self.sinkIsland(r, c - 1, m, n, grid)