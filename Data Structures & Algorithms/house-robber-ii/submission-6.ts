class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        if (nums.length < 2) {
            return nums[0]
        }
        
        let one = 0
        let two = 0

        for (let i = 0; i < nums.length - 1; i++) {
            [one, two] = [two, Math.max(two, one + nums[i])]
        }
        const res1 = Math.max(one, two)
        
        one = 0
        two = 0

        for (let i = 1; i < nums.length; i++) {
            [one, two] = [two, Math.max(two, one + nums[i])]
        }
        const res2 = Math.max(one, two)

        return Math.max(res1, res2)

    }
}
