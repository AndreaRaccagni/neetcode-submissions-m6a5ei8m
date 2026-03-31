class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def computeArea(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            for moveRow, moveCol in directions:
                area += computeArea(grid, r + moveRow, c + moveCol)

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = computeArea(grid, r, c)
                    maxArea = max(area, maxArea)

        return maxArea
