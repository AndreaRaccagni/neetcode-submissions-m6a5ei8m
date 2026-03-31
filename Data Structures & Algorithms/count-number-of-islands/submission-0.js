class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        let islands = 0

        if (!grid.length) return islands

        const n = grid[0].length
        const m = grid.length

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (grid[i][j] === '1') {
                    islands++
                    this.sinkIsland(grid, i, j, m, n)
                }
            }
        }
        return islands
    };

    sinkIsland(grid, row, col, m, n) {
        if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] === '0') return

        grid[row][col] = '0'

        this.sinkIsland(grid, row - 1, col, m, n)
        this.sinkIsland(grid, row + 1, col, m, n)
        this.sinkIsland(grid, row, col - 1, m, n)
        this.sinkIsland(grid, row, col + 1, m, n)
        return grid
    }
}
