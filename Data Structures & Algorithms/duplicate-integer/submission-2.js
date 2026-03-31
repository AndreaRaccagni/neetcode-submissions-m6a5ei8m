class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsMap = {}

        for(const num of nums){
            if(num in numsMap) return true
            numsMap[num] = 1
        }

        return false
    }
}
