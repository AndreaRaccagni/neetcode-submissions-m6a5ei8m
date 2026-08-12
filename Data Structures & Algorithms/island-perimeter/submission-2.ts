class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    islandPerimeter(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        const visited = new Set()

        function dfs(r: number, c: number): number {
            if (Math.min(r, c) < 0 || r >= ROWS || c >= COLS || grid[r][c] === 0) {
                return 1
            }

            if (visited.has(`#${r}#${c}`)) {
                return 0
            }

            visited.add(`#${r}#${c}`)

            return dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        }

        for (let r = 0; r < ROWS; r++){
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === 1) {
                    return dfs(r, c)
                }
            }
        }
        return 0
    }
}
