class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        let paths = 0
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        const seen = new Set<string>()

        function dfs(r: number, c: number) {
            if (Math.min(r, c) < 0 || r >= ROWS || c >= COLS || grid[r][c] === 1 || seen.has(`r${r}c${c}`)) {
                return
            }

            if (r === ROWS - 1 && c === COLS - 1) {
                paths++
                return
            }

            seen.add(`r${r}c${c}`)

            for (const [dr, dc] of directions) {
                dfs(r + dr, c + dc)
            }

            seen.delete(`r${r}c${c}`)
        }

        dfs(0, 0)
        return paths
    }
}
