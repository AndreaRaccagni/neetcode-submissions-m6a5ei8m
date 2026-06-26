class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                paths[r][c] = paths[r - 1][c] + paths[r][c - 1]
                
        return paths[m - 1][n - 1]