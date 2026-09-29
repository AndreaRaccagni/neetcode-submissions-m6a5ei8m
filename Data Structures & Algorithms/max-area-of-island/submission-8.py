class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_area = self.computeArea(grid, r, c, ROWS, COLS)
                    max_area = max(max_area, curr_area)

        return max_area


    def computeArea(self, grid, r, c, m, n):
        if min(r, c) < 0 or r >= m or c >= n or grid[r][c] != 1:
            return 0

        grid[r][c] = 0

        return (
            1
            + self.computeArea(grid, r + 1, c, m, n)
            + self.computeArea(grid, r, c + 1, m, n)
            + self.computeArea(grid, r - 1, c, m, n)
            + self.computeArea(grid, r, c - 1, m, n)
        )
