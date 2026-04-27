class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return 0

        seen = set()
        paths = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            nonlocal paths
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 1 or (r, c) in seen:
                return

            if r == rows - 1 and c == cols - 1:
                paths += 1
                return

            seen.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            seen.remove((r, c))
            
        dfs(0, 0)
        return paths