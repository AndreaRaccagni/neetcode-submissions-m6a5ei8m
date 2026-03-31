class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const count = {}
        for (const num of nums){
            if (num in count){
                return true
            } else {
                count[num] = 1
            }
        }

        return false
    }
}
