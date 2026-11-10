class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen: Record<number, number> = {}

        for (let i = 0; i < nums.length; i++) {
            const match = target - nums[i]
            
            if (match in seen) return [seen[match], i]
            seen[nums[i]] = i
        }
    }
}
