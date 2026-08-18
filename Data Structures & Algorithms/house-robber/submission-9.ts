class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        let one = 0
        let two = 0

        for (const n of nums) {
            [one, two] = [two, Math.max(two, one + n)]
        }

        return Math.max(two, one)
    }
}
