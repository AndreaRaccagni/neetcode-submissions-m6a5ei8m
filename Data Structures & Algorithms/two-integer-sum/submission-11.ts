class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen: Map<number, number> = new Map()

        for (let i = 0; i < nums.length; i++) {
            const match = target - nums[i]

            if (seen.has(match)) {
                return [seen.get(match), i]
            }

            seen.set(nums[i], i)
        }

        return [-1, -1]
    }
}
