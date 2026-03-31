class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);
        const result = [];

        for (let i = 0, n = nums.length; i < n - 2; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue;
            
            let l = i + 1;
            let r = n - 1;

            while (l < r) {
                const sum = nums[i] + nums[l] + nums[r]

                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    result.push([nums[i], nums[l], nums[r]]);
                    r--;
                    l++;
                    while (l < r && nums[l] === nums[l - 1]) {
                        l++;
                    }
                }
            }
        }
        return result;
    }
}
