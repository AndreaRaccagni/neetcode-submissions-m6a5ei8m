class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        preMax = []
        currMax = 0
        for h in height:
            currMax = max(currMax, h)
            preMax.append(currMax)

        postMax = [0] * n
        currMax = 0
        for i in range(n - 1, -1, -1):
            currMax = max(currMax, height[i])
            postMax[i] = currMax
        
        water = 0
        for i in range(n):
            currWater = min(preMax[i], postMax[i]) - height[i]
            water += currWater if currWater > 0 else 0

        return water