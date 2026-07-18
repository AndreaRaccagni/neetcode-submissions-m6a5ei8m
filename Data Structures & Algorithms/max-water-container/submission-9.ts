class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let l = 0
        let r = heights.length - 1
        let maxArea = 0

        while (l < r) {
            const h = Math.min(heights[l], heights[r])
            const area = h * (r - l)
            maxArea = Math.max(maxArea, area)

            if (heights[l] > heights[r]) {
                r--
            } else {
                l++
            }
        }

        return maxArea
    }
}
