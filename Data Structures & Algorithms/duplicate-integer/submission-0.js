class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if(!nums.length) return false
        const numsSet = new Set(nums)
        return numsSet.size !== nums.length
    }
}
