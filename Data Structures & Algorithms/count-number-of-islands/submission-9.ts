class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid: string[][]): number {
        const ROWS = grid.length;
        const COLS = grid[0].length;
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];
        let islands = 0;

        function dfs(r: number, c: number): void {
            if (Math.min(r, c) < 0 || r >= ROWS || c >= COLS || grid[r][c] === '0') {
                return;
            }

            grid[r][c] = '0'
            for (const coord of directions) {
                const [dr, dc] = coord;
                dfs(dr + r, dc + c);
            }
        }   

        for (let i = 0; i < ROWS; i++) {
            for (let j = 0; j < COLS; j++) {
                if (grid[i][j] === '1') {
                    islands++;
                    dfs(i, j);
                }
            }
        }
        return islands;
    }
}
