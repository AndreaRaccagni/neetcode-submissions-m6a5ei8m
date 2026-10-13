class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        res = [row] * m


        for r in range(1, m):
            for c in range(1, n):
                res[r][c] = res[r - 1][c] + res[r][c - 1]

        return res[m - 1][n - 1]