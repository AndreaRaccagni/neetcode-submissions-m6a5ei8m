class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)

        left = [0 for _ in range(n)]
        leftMax = 0
        for i in range(n):
            left[i] = leftMax
            leftMax = max(leftMax, height[i])

        right = [0 for _ in range(n)]
        rightMax = 0
        for j in range(n - 1, -1, -1):
            right[j] = rightMax
            rightMax = max(rightMax, height[j])

        for i in range(n):
            currWater = min(right[i], left[i]) - height[i]
            if currWater > 0:
                water += min(right[i], left[i]) - height[i]

        return water
        


