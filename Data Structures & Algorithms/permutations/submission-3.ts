class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums: number[]): number[][] {
        let res: number[][] = [[]]

        for (const n of nums) {
            const curr = []
            for (const perm of res) {
                for (let i = 0; i <= perm.length; i++) {
                    const next = [...perm]
                    next.splice(i, 0, n)
                    curr.push(next)
                }
            }
            res = [...curr]
        }
        return res
    }
}
