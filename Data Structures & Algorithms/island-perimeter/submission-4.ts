class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    islandPerimeter(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        const seen = new Set<string>()

        const dfs = (r: number, c: number) => {
            if (Math.min(r, c) < 0 || r >= ROWS || c >= COLS || grid[r][c] === 0) {
                return 1
            }

            if (seen.has(`#${r}#${c}`)) return 0

            seen.add(`#${r}#${c}`)

            let perimeter = 0
            for (const [dr, dc] of directions) {
                perimeter += dfs(r + dr, c + dc)
            }
            return perimeter
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === 1) return dfs(r, c)
            }
        }
        return 0
    }
}
