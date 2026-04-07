class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, visited):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visited:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            visited.add((r, c))
            count = 0

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                count += dfs(r + dr, c + dc, visited)
            
            visited.remove((r, c))
            return count

        return dfs(0, 0, set())