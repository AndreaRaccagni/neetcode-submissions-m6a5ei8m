class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid: number[][]): void {
        const ROWS = grid.length
        const COLS = grid[0].length

        const q: [number, number][] = [] //queue

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] == 0) {
                    q.push([r, c])
                } 
            }
        }

        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        const INF = 2147483647
        let distance = 0
        let p = 0

        while (p < q.length) {
            const n = q.length
            for (let i = p; i < n; i++) {
                const [r, c] = q[p]
                p++

                for (const [dr, dc] of directions) {
                    const newRow = dr + r
                    const newCol = dc + c
                    if (newRow >= 0 && newCol >= 0 && newRow < ROWS && newCol < COLS && grid[newRow][newCol] === INF) {
                        grid[newRow][newCol] = distance + 1
                        q.push([newRow, newCol])
                    }
                }
            }

            distance++
        }
    }
}
