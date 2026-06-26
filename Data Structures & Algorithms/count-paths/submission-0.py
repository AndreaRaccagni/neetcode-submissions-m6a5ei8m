class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                left = paths[r - 1][c] if r - 1 >= 0 else 0
                top = paths[r][c - 1] if c - 1 >= 0 else 0

                paths[r][c] = left + top
                
        return paths[m - 1][n - 1]