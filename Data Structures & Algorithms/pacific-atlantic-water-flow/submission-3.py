class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, prev, ocean):
            if min(r, c) < 0 or r >= rows or c >= cols or heights[r][c] < prev or (r, c) in ocean:
                return

            ocean.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)

        #call dfs on edges
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)     

        res = []
        for cell in pac:
            if cell in atl:
                res.append(cell)

        return res

        