class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, prev, ocean):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or prev > heights[r][c] or (r, c) in ocean:
                return

            ocean.add((r, c))
            directions = [[1, 0],[0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)

        return list(atl.intersection(pac))

