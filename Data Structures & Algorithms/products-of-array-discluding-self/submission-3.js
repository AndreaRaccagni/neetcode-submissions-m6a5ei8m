class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length
        const forward = new Array(n).fill(1)
        const backward = new Array(n).fill(1)
        for (let i = 1; i < n; i++) {
            forward[i] = forward[i - 1] * nums[i - 1]
            backward[n - i - 1] = backward[n - i] * nums[n - i]
        }
        return forward.map((n, i) => n * backward[i])


    }
}
