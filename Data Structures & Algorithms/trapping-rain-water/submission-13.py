class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        maxLeft = height[l]
        r = n - 1
        maxRight = height[r]
        water = 0

        while l <= r:
            if maxLeft < maxRight:
                water += maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                water += maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
        return water