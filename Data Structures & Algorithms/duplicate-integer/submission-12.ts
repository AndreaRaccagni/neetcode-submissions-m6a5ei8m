class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const seen: Set<number> = new Set()

        for (const n of nums) {
            if (seen.has(n)) return true
            seen.add(n)
        }

        return false
    }
}
