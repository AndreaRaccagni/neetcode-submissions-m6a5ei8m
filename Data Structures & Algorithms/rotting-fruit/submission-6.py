class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rotten = deque()
        fresh = 0
        minutes = -1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        if not fresh:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while rotten:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1