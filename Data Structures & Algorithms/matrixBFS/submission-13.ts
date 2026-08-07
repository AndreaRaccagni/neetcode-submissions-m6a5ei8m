class Solution {
    /**
     * @param {number[][]}
     * @returns {number}
     */
    shortestPath(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        const visited = new Set<string>()
        const q = []
        let p = 0
        let level = 0
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        if (grid[0][0] === 0) {
            q.push([0, 0])
            visited.add(`r0c0`)
        }

        while (p < q.length) {
            const n = q.length
            while (p < n) {
                const [r, c] = q[p]
                if (r === ROWS - 1 && c === COLS - 1) {
                    return level
                }

                

                for (const [dr, dc] of directions) {
                    const nr = r + dr
                    const nc = c + dc
                    if (nr >= 0 && nc >= 0 && nr < ROWS && nc < COLS && grid[nr][nc] !== 1 && !visited.has(`r${nr}c${nc}`)) {
                        q.push([nr, nc])
                        visited.add(`r${nr}c${nc}`)
                    }
                }
                p++
            }
            level++
        }

        return -1
    }
}
