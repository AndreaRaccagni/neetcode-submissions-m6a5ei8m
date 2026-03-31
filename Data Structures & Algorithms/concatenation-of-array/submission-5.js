class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const ans = new Array(nums.length)
        const n = nums.length

        for (let i = 0; i < n; i++) {
            ans[i] = ans[i + n] = nums[i]
        }

        return ans
    }
}
