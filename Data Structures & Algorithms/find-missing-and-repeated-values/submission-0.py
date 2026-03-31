class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        n = len(grid)
        seen = set()

        for r in range(n):
            for c in range(n):
                if grid[r][c] in seen:
                    res.append(grid[r][c])
                
                seen.add(grid[r][c])

        for i in range(1, n * n + 1):
            if i not in seen:
                res.append(i)
                return res