class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def getIslandArea(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in dimensions:
                area += getIslandArea(grid, r + dr, c + dc)

            return area

        for r in range(rows):
            for c in range(cols):
                currArea = getIslandArea(grid, r, c)
                maxArea = max(currArea, maxArea)
        return maxArea
