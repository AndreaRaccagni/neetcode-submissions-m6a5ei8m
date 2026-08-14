class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n: number): number {
        let one = 1
        let two = 1

        for (let _i = 1; _i < n; _i++) {
            [one, two] = [two, one + two]
        }

        return two
    }
}
