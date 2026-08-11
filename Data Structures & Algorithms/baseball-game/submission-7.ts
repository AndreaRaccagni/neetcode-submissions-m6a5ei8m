class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations: string[]): number {
        const scores = []
        let total = 0

        for (const op of operations) {
            let newScore = 0
            if (op === '+') {
                newScore = scores[scores.length - 1] + scores[scores.length - 2]
                scores.push(newScore)
            } else if (op === 'D') {
                newScore = scores[scores.length - 1] * 2
                scores.push(newScore)
            } else if (op === 'C') {
                newScore = scores.pop() * -1
            } else {
                newScore = parseInt(op)
                scores.push(newScore)
            }

            total += newScore
        }

        return total
    }
}
