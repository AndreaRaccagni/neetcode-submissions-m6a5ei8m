class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        if (!nums || !nums.length) return null

        let l = 0;
        let r = nums.length - 1;

        while (l < r) {
            const mid = Math.floor((r - l) / 2 + l);

            if (nums[r] >= nums[mid]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return nums[l]
    }
}
