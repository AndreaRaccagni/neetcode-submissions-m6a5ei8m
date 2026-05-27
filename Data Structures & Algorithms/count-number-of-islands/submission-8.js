class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        if (!grid.length) {
            return 0
        }

        const ROWS = grid.length
        const COLS = grid[0].length
        let islands = 0

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    this.sinkIsland(grid, r, c, ROWS, COLS)
                    islands++
                }
            }
        }
        return islands
    }

    sinkIsland(grid, r, c, m, n) {
        if (Math.min(r, c) < 0 || r >= m || c >= n || grid[r][c] == '0') return

        grid[r][c] = '0'
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for (const [dr, dc] of directions) {
            this.sinkIsland(grid, r + dr, c + dc, m, n)
        }
    }
}
