class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        count = 0
        if not grid:
            return count

        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c, visited):
            nonlocal count
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visited:
                return

            if r == rows - 1 and c == cols - 1:
                count += 1
                return

            visited.add((r, c))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                dfs(grid, r + dr, c + dc, visited)
            
            visited.remove((r, c))

        dfs(grid, 0, 0, set())
        return count