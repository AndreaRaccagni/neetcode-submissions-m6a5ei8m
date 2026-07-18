class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height: number[]): number {
        const fromLeft: number[] = new Array(height.length).fill(0) 
        let maxHeight = 0
        for (let i = 0; i < height.length; i++) {
            maxHeight = Math.max(maxHeight, height[i])
            fromLeft[i] = maxHeight
        }

        const fromRight: number[] = new Array(height.length).fill(0) 
        maxHeight = 0
        for (let i = height.length - 1; i >= 0; i--) {
            maxHeight = Math.max(maxHeight, height[i])
            fromRight[i] = maxHeight
        }

        let water = 0
        for (let i = 0; i < height.length; i++) {
            const h = Math.min(fromLeft[i], fromRight[i])
            water += h - height[i]
        }

        return water
    }
}
