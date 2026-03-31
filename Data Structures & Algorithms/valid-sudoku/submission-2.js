class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        return this.checkRows(board) && this.checkColumns(board) && this.checkSquare(board)
    }

    checkRows(board) {
        for (const row of board) {
            const seen = new Set()
            for (const num of row) {
                if (num !== '.' && seen.has(num)) {
                    return false
                }
                seen.add(num)
            }
        }

        return true
    }

    checkColumns(board) {
        const n = board.length
        for (let i = 0; i < n; i++) {
            const seen = new Set()
            for (let j = 0; j < n; j++) {
                const num = board[j][i]
                if (num !== '.' && seen.has(num)) {
                    return false
                }
                seen.add(num)
            }
        }
    return true
    }

    checkSquare(board) {
        const n = board.length
        const squaresMap = {}

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                const x = Math.floor(i / 3)
                const y = Math.floor(j / 3)

                const key = `${x}${y}`
                const num = board[i][j]

                if (num == '.') {
                    continue
                }

                if (!(key in squaresMap)) {
                    squaresMap[key] = new Set([num])
                    continue
                }

                if (squaresMap[key].has(num)) {
                    return false
                }

                squaresMap[key].add(num) 

            }
        }

        return true
    }
}
