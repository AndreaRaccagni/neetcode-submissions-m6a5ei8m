class Solution {
    shortestPath(grid: number[][]): number {
        const ROWS = grid.length
        const COLS = grid[0].length

        if (grid[0][0] === 1) {
            return -1
        }

        const q: [number, number][] = [[0, 0]]
        let head = 0
        let steps = 0

        const directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        grid[0][0] = 1

        while (head < q.length) {
            const levelEnd = q.length

            while (head < levelEnd) {
                const [r, c] = q[head++]

                if (r === ROWS - 1 && c === COLS - 1) {
                    return steps
                }

                for (const [dr, dc] of directions) {
                    const nr = r + dr
                    const nc = c + dc

                    if (
                        nr >= 0 &&
                        nc >= 0 &&
                        nr < ROWS &&
                        nc < COLS &&
                        grid[nr][nc] === 0
                    ) {
                        grid[nr][nc] = 1
                        q.push([nr, nc])
                    }
                }
            }

            steps++
        }

        return -1
    }
}