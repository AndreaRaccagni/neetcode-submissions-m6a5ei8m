class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        if (nums.length === 0) return 0;
        if (nums.length === 1) return nums[0];

        let one = 0
        let two = 0

        for (let i = 0; i < nums.length - 1; i++) {
            [one, two] = [two, Math.max(two, one + nums[i])]
        }
        const res1 = two
        
        one = 0
        two = 0

        for (let i = 1; i < nums.length; i++) {
            [one, two] = [two, Math.max(two, one + nums[i])]
        }

        return Math.max(res1, two)

    }
}
