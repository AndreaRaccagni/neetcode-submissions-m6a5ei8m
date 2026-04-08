class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        q = deque([[0, 0]])
        count = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return count

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    nextRow = r + dr
                    nextCol = c + dc
                    if 0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == 0:
                        grid[nextRow][nextCol] = 1
                        q.append([nextRow, nextCol])
            count += 1

        return -1