class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numsSet = new Set(nums)
        let longest = 0

        for (const num of nums) {
            if (numsSet.has(num - 1)) {
                continue
            }
            
            let curr = num
            let length = 1
            while (numsSet.has(curr + 1)) {
                length ++
                curr ++
            }

            longest = Math.max(longest, length)
        }

        return longest
    }
}
