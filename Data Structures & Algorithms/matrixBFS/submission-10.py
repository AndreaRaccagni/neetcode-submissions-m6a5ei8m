class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1


        steps = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque([(0, 0)])
        grid[0][0] = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return steps

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 1
            steps += 1

        return -1