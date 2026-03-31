class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let i = 0;
        let count = 1;

        while(nums[i + 1] != undefined){
            if (nums[i] !== nums[i + 1]){
                count++
                i++
            } else {
                nums.splice(i + 1, 1);
            }
        }

        return count
    }
}
