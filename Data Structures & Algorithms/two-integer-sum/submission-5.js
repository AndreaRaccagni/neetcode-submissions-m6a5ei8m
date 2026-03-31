class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numsMap = {}

        for (let i = 0, n = nums.length; i < n; i++){
            numsMap[nums[i]] = i;
        }

        for (let i = 0, n = nums.length; i < n; i++){
            const match = target - nums[i];
            if (match in numsMap && i !== numsMap[match]) {
                return [i, numsMap[match]];
            }
        }

    }
}
