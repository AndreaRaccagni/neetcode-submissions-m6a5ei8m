class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsMap = {}

        for(const num of nums){
            numsMap[num] = (numsMap[num] || 0) + 1
        }

        for(const key in numsMap){
            if(numsMap[key] > 1){
                return true
            }
        }

        return false
    }
}
