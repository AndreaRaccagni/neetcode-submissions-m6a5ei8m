class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        if grid[rows - 1][cols - 1] == 1:
            return 0

        count = 0
        visited = set()

        def dfs(r, c):
            nonlocal count

            if min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 1:
                return

            if r == rows - 1 and c == cols - 1:
                count += 1
                return

            visited.add((r, c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            visited.remove((r, c))
           
        dfs(0, 0)
        return count