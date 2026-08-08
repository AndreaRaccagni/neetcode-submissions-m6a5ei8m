class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums: number[]): number {
        let currElement = nums[0]
        let count = 0

        for (const n of nums) {
            if (count == 0) {
                currElement = n
            }
            
            if (n === currElement) {
                count += 1
            } else {
                count -= 1
            }
        }
        return currElement
    }
}
