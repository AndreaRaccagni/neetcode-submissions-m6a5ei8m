class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                res[r][c] = res[r - 1][c] + res[r][c - 1]

        return res[m - 1][n - 1]