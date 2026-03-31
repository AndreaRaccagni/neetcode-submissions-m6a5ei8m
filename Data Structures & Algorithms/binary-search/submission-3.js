class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0
        let r = nums.length - 1

        while (l <= r){
            const mid = Math.floor((r + l) / 2)

            if (target < nums[mid]) {
                r = mid - 1
            } else if (target > nums[mid]) {
                l = mid + 1
            } else {
                return mid
            }
        }
        return -1
    }
}
