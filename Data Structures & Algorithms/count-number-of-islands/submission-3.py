class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def sinkIsland(grid, row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                sinkIsland(grid, row + dr, col + dc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    sinkIsland(grid, i, j)
        
        return islands
