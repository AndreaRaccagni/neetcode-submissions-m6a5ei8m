class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const n = board.length
        const rows = Array.from({length: n}, () => new Set())
        const cols = Array.from({length: n}, () => new Set())
        const squares = Array.from({length: n}, () => new Set())
        const squareSize = 3

        for (let row = 0; row < n; row++){
            for (let col = 0; col < n; col++){
                const num = board[row][col]

                if (board[row][col] === '.') continue;

                const squareKey = Math.floor(row / squareSize) * squareSize + Math.floor(col / squareSize)

                if(rows[row].has(num) || cols[col].has(num) || squares[squareKey].has(num)){
                    return false
                }

                rows[row].add(num)
                cols[col].add(num)
                squares[squareKey].add(num)
            }
        }
        
        return true
    }
}
