class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    count += 1
                    self.sinkIsland(grid, r, c, ROWS, COLS)

        return count


    def sinkIsland(self, grid, r, c, m, n):
        if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for dr, dc in directions:
            self.sinkIsland(grid, r + dr, c + dc, m, n)