class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;
        let maxAmount = 0;

        while (left < right) {
            const currentAmount = (right - left) * Math.min(heights[left], heights[right])
            maxAmount = Math.max(maxAmount, currentAmount)
            
            heights[left] < heights[right] ? left++ : right--
        }

        return maxAmount
    }
}
