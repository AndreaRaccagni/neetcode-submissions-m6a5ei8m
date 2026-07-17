class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const numsSet = new Set(nums)
        let maxCount = 0

        for (const n of nums) {
            let count = 0
            if (!numsSet.has(n - 1)) {
                let curr = n
                while (numsSet.has(curr)) {
                    count++
                    curr++
                }

                maxCount = Math.max(maxCount, count)
            }
        }

        return maxCount
    }
}
