class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        p = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += r + 1 >= rows or grid[r + 1][c] == 0
                    p += c + 1 >= cols or grid[r][c + 1] == 0
                    p += r - 1 < 0 or grid[r - 1][c] == 0
                    p += c - 1 < 0 or grid[r][c - 1] == 0

        return p