class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = {}

        for(let i = 0; i < nums.length; i++){
            const missing = target - nums[i]
            if (missing in seen) {
                return[seen[missing], i]
            }

            seen[nums[i]] = i
        }

        return []
    }
}
