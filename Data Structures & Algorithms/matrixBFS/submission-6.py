class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        moves = 0
        q = deque([[0, 0]])
        grid[0][0] = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                if r == rows - 1 and c == cols - 1:
                    return moves

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    newRow = r + dr
                    newCol = c + dc

                    if newRow >= 0 and newCol >= 0 and newRow < rows and newCol < cols and grid[newRow][newCol] == 0:
                        q.append([newRow, newCol])
                        grid[newRow][newCol] = 1

            moves += 1

        return -1