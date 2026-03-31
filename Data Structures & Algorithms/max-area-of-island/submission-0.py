class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0

        def computeArea(grid, r, c):
            nonlocal area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return

            grid[r][c] = 0
            area += 1

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                computeArea(grid, r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                if grid[r][c] == 1:
                    computeArea(grid, r, c)
                    maxArea = max(maxArea, area)
   
        return maxArea
