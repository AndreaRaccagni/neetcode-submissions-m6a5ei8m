class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        INF = 2 ** 31 - 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        distance = 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    newRow = r + dr
                    newCol = c + dc
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == INF:
                        q.append([newRow, newCol])
                        grid[newRow][newCol] = distance + 1

            distance += 1
