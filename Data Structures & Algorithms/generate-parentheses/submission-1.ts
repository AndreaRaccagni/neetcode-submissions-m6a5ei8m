class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n: number): string[] {
        const res = []
        this.backtrack(res, '', n, 0, 0)
        return res
    }

    backtrack(res: string[], curr: string, n: number, open: number, close: number): void {
        if (close === open && open === n) {
            res.push(curr)
            return
        }

        if (open < n) {
            this.backtrack(res, curr + '(', n, open + 1, close)
        }

        if (close < open) {
            this.backtrack(res, curr + ')', n, open, close + 1)
        }
    }
}
