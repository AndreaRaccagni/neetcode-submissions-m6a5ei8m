class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        const n = 3
        return this.isValidRowsAndCols(board, n * n) && this.isValidSquares(board, n)
    }

    isValidRowsAndCols(board: string[][], n: number): boolean {
        for (let i = 0; i < n; i++) {
            const row = new Set()
            const col = new Set()
            for (let j = 0; j < n; j++) {
                if (board[i][j] != '.' && row.has(board[i][j])){
                    return false
                } else if (board[j][i] != '.' && col.has(board[j][i])) {
                    return false
                }
                row.add(board[i][j])
                col.add(board[j][i])
            }
        }
        return true
    }

    isValidSquares(board: string[][], n: number): boolean {
        const edge = n * n
        for (let r = 0; r < edge; r += n) {
            for (let c = 0; c < edge; c += n) {
                const square = new Set()

                for (let i = r; i < r + n; i++) {
                    for (let j = c; j < c + n; j++ ) {
                        if (board[i][j] != '.' && square.has(board[i][j])) {
                            return false
                        }
                        square.add(board[i][j])
                    }
                }
            }
        }
        return true
    }
}
