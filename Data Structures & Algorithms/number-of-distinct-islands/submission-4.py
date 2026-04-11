class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct = set()
        rows = len(grid)
        cols = len(grid[0])

        def sinkAndMapIsland(r, c, code):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return ""

            grid[r][c] = 0
            path = code

            directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

            for dr, dc, move in directions:
                path += self.sinkAndMapIsland(r + dr, c + dc, move)

            path += "B"
            return path

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    hashedIsland = self.sinkAndMapIsland(r, c, rows, cols, grid, "S")
                    distinct.add(hashedIsland)

        return len(distinct)

    def sinkAndMapIsland(self, r, c, m, n, grid, code):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
            return ""

        grid[r][c] = 0
        path = code

        directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

        for dr, dc, move in directions:
            path += self.sinkAndMapIsland(r + dr, c + dc, m, n, grid, move)

        path += "B"
        return path