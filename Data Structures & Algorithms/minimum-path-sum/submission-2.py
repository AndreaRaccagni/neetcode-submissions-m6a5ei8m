class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = []
        for r in range(m):
            res.append([])
            for c in range(n):
                res[r].append(grid[r][c])

        for r in range(1, m):
            res[r][0] = res[r][0] + res[r - 1][0]
        
        for c in range(1, n):
            res[0][c] = res[0][c] + res[0][c - 1]

        for r in range(1, m):
            for c in range(1, n):
                res[r][c] += min(res[r][c - 1], res[r - 1][c])


        return res[-1][-1]
