class Solution {
    /**
     * @param {number[]} nums
     * @return {string}
     */
    largestNumber(nums) {
        nums = nums.map(n => n.toString())
        nums.sort((a, b) => (b + a).localeCompare(a + b))
        return nums[0] !== '0' ? nums.join('') : '0'
    }
}
