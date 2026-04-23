class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == '1':
                    self.sinkIsland(r, c, rows, cols, grid)
                    islands += 1

        return islands
    
    def sinkIsland(self, r, c, rows, cols, grid):
        if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for dr, dc in directions:
            self.sinkIsland(r + dr, c + dc, rows, cols, grid)
