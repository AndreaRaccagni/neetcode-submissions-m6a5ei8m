class Solution {
    /**
     * @param {number} n
     * @param {number} k
     * @return {number[][]}
     */
    combine(n: number, k: number): number[][] {
        const res: number[][]  = []

        const backtracking = (i: number, curr: number[]): void => {
            if (i > n) {
                if (curr.length === k) {
                    res.push([...curr])
                }
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
