class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = self.computeArea(r, c, ROWS, COLS, grid, 0)
                    maxArea = max(area, maxArea)

        return maxArea

    
    def computeArea(self, r, c, m, n, grid, area):
        if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        area = 1

        area += self.computeArea(r + 1, c, m, n, grid, area)
        area += self.computeArea(r, c + 1, m, n, grid, area)
        area += self.computeArea(r - 1, c, m, n, grid, area)
        area += self.computeArea(r, c - 1, m, n, grid, area)
        return area