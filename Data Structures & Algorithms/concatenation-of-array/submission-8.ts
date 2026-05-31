class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        const n: number = nums.length
        const res: number[] = new Array(n * 2).fill(0)


        for (let i = 0; i < n; i++) {
            res[i] = res[i + n] = nums[i]
        }

        return res
    }
}
