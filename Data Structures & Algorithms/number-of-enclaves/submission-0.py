class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def sinkIsland(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            
            grid[r][c] = 0

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for moveRow, moveCol in directions:
                sinkIsland(grid, r + moveRow, c + moveCol)

        for r in range(0, rows, rows - 1):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                sinkIsland(grid, r, c)

        for r in range(rows):
            for c in range(0, cols, cols - 1):
                if grid[r][c] == 0:
                    continue

                sinkIsland(grid, r, c)

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                count += 1 if grid[r][c] == 1 else 0

        return count
