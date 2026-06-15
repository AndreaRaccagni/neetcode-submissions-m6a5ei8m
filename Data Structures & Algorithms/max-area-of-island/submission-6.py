class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area
