class Solution {
    /**
     * @param {number} n
     * @param {number} k
     * @return {number[][]}
     */
    combine(n: number, k: number): number[][] {
        const res: number[][]  = []

        const backtracking = (i: number, curr: number[]): void => {
            if (curr.length === k) {
                res.push([...curr])
                return
            }

            if (i > n) {
                return
            }

            curr.push(i)
            backtracking(i + 1, curr)
            curr.pop()
            backtracking(i + 1, curr)
        }

        backtracking(1, [])
        return res
    }
}
