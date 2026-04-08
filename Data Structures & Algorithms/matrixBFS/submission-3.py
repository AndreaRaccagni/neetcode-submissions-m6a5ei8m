class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        q = deque([[0, 0]])
        grid[0][0] = 1
        count = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return count

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append([nr, nc])

            count += 1

        return -1