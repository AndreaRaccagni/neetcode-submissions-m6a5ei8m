
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const n = nums.length
        const res = new Array(n * 2).fill(0)


        for (let i = 0; i < n; i++) {
            res[i] = res[i + n] = nums[i]
        }

        return res
    }
}
