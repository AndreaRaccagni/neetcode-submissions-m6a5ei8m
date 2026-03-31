class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b)
        const result = []

        for (let i = 0, n = nums.length; i < n - 2; i++) {
            while (i > 0 && nums[i - 1] === nums[i]) {
                i++
            }
            let l = i + 1
            let r = n - 1

            while (l < r) {
                const total = nums[i] + nums[l] + nums[r]
                if (total > 0) {
                    r--
                } else if (total < 0) {
                    l++
                } else {
                    result.push([nums[i], nums[l], nums[r]])
                    l++
                    r--
                    while (l < r && nums[l - 1] === nums[l]) {
                        l++
                    }
                    while (l < r && nums[r + 1] === nums[r]) {
                        r--
                    }
                }
            }
        }
        return result
    }
}
