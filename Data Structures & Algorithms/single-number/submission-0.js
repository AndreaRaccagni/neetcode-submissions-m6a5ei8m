class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        return nums.reduce((acc, curr) => acc^curr, 0)
    }
}
