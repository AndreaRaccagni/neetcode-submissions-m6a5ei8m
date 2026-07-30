class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        let maxArea = 0
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c]) {
                    const area = this.sinkIsland(grid, r, c, ROWS, COLS, directions)
                    maxArea = Math.max(area, maxArea)
                }
            }
        }
        return maxArea
    }

    sinkIsland(grid: number[][], r: number, c: number, m: number, n: number, directions: number[][]): number {
        if (Math.min(r, c) < 0 || r >= m || c >= n || grid[r][c] == 0) {
            return 0
        }

        grid[r][c] = 0
        let area = 1

        for (const coord of directions) {
            const [dr, dc] = coord
            area += this.sinkIsland(grid, r + dr, c + dc, m, n, directions)
        }

        return area
    }
}
