class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height: number[]): number {
        let l = 0;
        let r = height.length - 1;
        let maxLeft = height[l];
        let maxRight = height[r];
        let water = 0;

        while (l < r) {
            if (maxLeft > maxRight) {
                r--;
                maxRight = Math.max(maxRight, height[r]);
                water += maxRight - height[r];
            } else {
                l++;
                maxLeft = Math.max(maxLeft, height[l]);
                water += maxLeft - height[l];
            }
        }

        return water;
    }
}
