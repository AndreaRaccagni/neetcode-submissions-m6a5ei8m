class Solution {
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board: string[][]): void {
        const ROWS = board.length
        const COLS = board[0].length
        const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        function dfs(r: number, c: number) {
            if (Math.min(r, c) < 0 || r >= ROWS || c >= COLS || board[r][c] !== 'O') {
                return
            }

            board[r][c] = 'C'

            for (const [dc, dr] of directions) {
                dfs(r + dr, c + dc)
            }
        }

        for (let r = 0; r < ROWS; r++) {
            dfs(r, 0)
            dfs(r, COLS - 1)
        }

        for (let c = 0; c < COLS; c++) {
            dfs(0, c)
            dfs(ROWS - 1, c)
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++){
                if (board[r][c] == 'C') {
                    board[r][c] = 'O'
                } else if (board[r][c] == 'O') {
                    board[r][c] = 'X'
                }
            }
        }
    }
}
