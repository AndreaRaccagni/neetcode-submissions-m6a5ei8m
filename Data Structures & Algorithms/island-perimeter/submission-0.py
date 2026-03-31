class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        p = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    p += (r + 1 >= ROWS or grid[r + 1][c] == 0)
                    p += (c + 1 >= COLS or grid[r][c + 1] == 0)
                    p += (r - 1 < 0 or grid[r - 1][c] == 0)
                    p += (c - 1 < 0 or grid[r][c - 1] == 0)

        return p