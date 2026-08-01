class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights: number[][]): number[][] {
        const ROWS = heights.length
        const COLS = heights[0].length
        const atl = new Set<string>()
        const pac = new Set<string>()
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for (let r = 0; r < ROWS; r++) {
            this.dfs(heights, r, 0, ROWS, COLS, heights[r][0], pac, directions)
            this.dfs(heights, r, COLS - 1, ROWS, COLS, heights[r][COLS - 1], atl, directions)
        }

        for (let c = 0; c < COLS; c++) {
            this.dfs(heights, 0, c, ROWS, COLS, heights[0][c], pac, directions)
            this.dfs(heights, ROWS - 1, c, ROWS, COLS, heights[ROWS - 1][c], atl, directions)
        }
        
        const res: string[] = []
        for (const coord of atl) {
            if (pac.has(coord)) {
                res.push(coord)
            }
        }

        return res.map(coordStr => {
            const coord = coordStr.split(';')
            return [Number(coord[0]), Number(coord[1])]
        })
    }

    dfs(heights: number[][], r: number, c: number, m: number, n: number, prev: number, ocean: Set<string>, directions: number[][]) {
        if (r < 0 || c < 0 || r >= m || c >= n || prev > heights[r][c] || ocean.has(`${r};${c}`)) {
            return
        }

        ocean.add(`${r};${c}`)


        for (const [dr, dc] of directions) {
            this.dfs(heights, r + dr, c + dc, m, n, heights[r][c], ocean, directions)
        }
    }
}
