class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [0] * (n * n + 1)
        res = [-1, -1]

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        for i in range(1, len(count)):
            c = count[i]

            if c == 2:
                res[0] = i
            elif c == 0:
                res[1] = i

        return res