class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])    
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = self.sinkIsland(grid, r, c, ROWS, COLS)
                    maxArea = max(area, maxArea)

        return maxArea


    def sinkIsland(self, grid, r, c, m , n):
        if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        area = 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for dr, dc in directions:
            area += self.sinkIsland(grid, r + dr, c + dc, m, n)

        return area
