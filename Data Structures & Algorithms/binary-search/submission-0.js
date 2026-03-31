class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let i = 0;
        let j = nums.length - 1

        while (i <= j){
            const middle_index = Math.floor((j + i) / 2)

            if (nums[middle_index] > target){
                j = middle_index - 1
            } else if (nums[middle_index] < target){
                i = middle_index + 1
            } else {
                return middle_index
            }
        }

        return -1
    }
}
