class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)

        right = [0 for _ in range(n)]
        rightMax = 0
        for i in range(n):
            right[i] = rightMax
            rightMax = max(rightMax, height[i])

        left = [0 for _ in range(n)]
        leftMax = 0
        for j in range(n - 1, -1, -1):
            left[j] = leftMax
            leftMax = max(leftMax, height[j])

        for i in range(n):
            currWater = min(right[i], left[i]) - height[i]
            if currWater > 0:
                water += min(right[i], left[i]) - height[i]

        return water
        


