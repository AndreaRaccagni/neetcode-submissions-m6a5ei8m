class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    numSubarrayProductLessThanK(nums: number[], k: number): number {
        let res = 0;
        let l = 0;
        let product = 1;

        for (let r = 0; r < nums.length; r++) {
            product *= nums[r]
            while (l <= r && product >= k) {
                product = Math.floor(product / nums[l])
                l++
            }
            res += r - l + 1
        }

        return res
    }
}
