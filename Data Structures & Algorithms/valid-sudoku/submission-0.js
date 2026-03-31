class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const n = board.length
        const numbersMap = {}
        const squareSize = 3

        for (let row = 0; row < n; row++){
            for (let col = 0; col < n; col++){
                const num = board[row][col]

                if (board[row][col] === '.') continue;

                const squareKey = `${Math.floor(row / squareSize)}${Math.floor(col / squareSize)}`
                console.log(num, row, col, squareKey)

                if (!(num in numbersMap)) {
                    const position = {
                        x: new Set([row]),
                        y: new Set([col]),
                        square: new Set([squareKey])
                    }
                    
                    numbersMap[num] = position
                } else {
                    const sameRow = numbersMap[num].x.has(row)
                    const sameCol = numbersMap[num].y.has(col)
                    const sameSquare = numbersMap[num].square.has(squareKey)

                    if (sameRow || sameCol || sameSquare) return false
                        
                    numbersMap[num].x.add(row)
                    numbersMap[num].y.add(col)
                    numbersMap[num].square.add(squareKey)
                }
            }
        }
        
        return true
    }
}
