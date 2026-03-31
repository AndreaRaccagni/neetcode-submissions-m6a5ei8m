class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        treasures = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasures.append((r, c))

        INF = 2 ** 31 - 1
        q = deque(treasures)
        count = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                print(r, c)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                        grid[nr][nc] = count + 1
                        q.append((nr, nc))
            
            count += 1




