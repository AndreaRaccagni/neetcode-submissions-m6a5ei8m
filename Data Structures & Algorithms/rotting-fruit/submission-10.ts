class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length
        let fresh = 0
        let sources: [number, number][] = []

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === 1) {
                    fresh++
                } else if (grid[r][c] === 2) {
                    sources.push([r, c])
                }
            }
        }

        let head = 0
        let time = 0
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while (fresh && head < sources.length) {
            let n = sources.length
            for (let i = head; i < n; i++){
                const [r, c] = sources[head++]

                for (const [dr, dc] of directions) {
                    const newRow = r + dr
                    const newCol = c + dc
                    if (newRow >= 0 && newCol >= 0 && newRow < ROWS && newCol < COLS && grid[newRow][newCol] === 1) {
                        grid[newRow][newCol] = 2
                        fresh--
                        sources.push([newRow, newCol])
                    }
                }
            }
            time++
        }
        return fresh === 0 ? time : -1
    }
}
