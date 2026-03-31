class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()
        
        if grid[0][0] != 1:
            q.append((0, 0))
        
        count = 1
        directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == n - 1 and c == n - 1:
                    return count

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

            count += 1
        
        return -1
