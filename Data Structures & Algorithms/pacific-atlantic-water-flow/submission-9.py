class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))

        def dfs(r, c, ocean):
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in ocean or heights[nr][nc] < heights[r][c]:
                    continue

                ocean.add((nr, nc))
                dfs(nr, nc, ocean)

        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        return list(pac.intersection(atl))