class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        for (const num of nums) {
            const index = Math.abs(num) - 1
            if (nums[index] < 0) {
                return index + 1
            }

            nums[index] *= -1
        }
    }
}