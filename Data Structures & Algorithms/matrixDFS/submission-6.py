class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()

        def dfs(coordinates):
            nonlocal count
            r, c = coordinates
            
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 1 or coordinates in visited:
                return

            if r == rows - 1 and c == cols - 1:
                count += 1
                return

            visited.add(coordinates)

            dfs((r + 1, c))
            dfs((r, c + 1))
            dfs((r - 1, c))
            dfs((r, c - 1))

            visited.remove(coordinates)

        dfs((0, 0))
        return count