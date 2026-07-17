class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const prefix = new Array(nums.length).fill(1)

        for (let i = 0; i < nums.length - 1; i++) {
            prefix[i + 1] = nums[i] * prefix[i]
        }

        let prod = 1

        for (let i = nums.length - 1; i >= 0; i--) {
            prefix[i] *= prod
            prod *= nums[i]
        }

        return prefix
    }
}
