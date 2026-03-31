class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length
        const result = new Array(n).fill(1)
        
        for (let i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1]
        }

        let back = 1
        for (let i = n - 1; i >= 0; i--) {
            result[i] *= back
            back *= nums[i]           
        }

        return result
    }
}
