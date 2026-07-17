class Solution {
    isValidSudoku(board: string[][]): boolean {
        const squareSize = 3

        return (
            this.isValidRowsAndCols(board, squareSize * squareSize) &&
            this.isValidSquares(board, squareSize)
        )
    }

    isValidRowsAndCols(board: string[][], size: number): boolean {
        for (let i = 0; i < size; i++) {
            const row = new Set<string>()
            const col = new Set<string>()

            for (let j = 0; j < size; j++) {
                const rowValue = board[i][j]
                const colValue = board[j][i]

                if (rowValue !== ".") {
                    if (row.has(rowValue)) return false
                    row.add(rowValue)
                }

                if (colValue !== ".") {
                    if (col.has(colValue)) return false
                    col.add(colValue)
                }
            }
        }

        return true
    }

    isValidSquares(board: string[][], squareSize: number): boolean {
        const boardSize = squareSize * squareSize

        for (let rowStart = 0; rowStart < boardSize; rowStart += squareSize) {
            for (let colStart = 0; colStart < boardSize; colStart += squareSize) {
                const square = new Set<string>()

                for (
                    let row = rowStart;
                    row < rowStart + squareSize;
                    row++
                ) {
                    for (
                        let col = colStart;
                        col < colStart + squareSize;
                        col++
                    ) {
                        const value = board[row][col]

                        if (value !== ".") {
                            if (square.has(value)) return false
                            square.add(value)
                        }
                    }
                }
            }
        }

        return true
    }
}