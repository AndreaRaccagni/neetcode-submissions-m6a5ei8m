class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        maxHeights =[[] for _ in range(n)]
        currMax = 0
        for i in range(n):
            maxHeights[i].append(currMax)
            currMax = max(currMax, height[i])

        currMax = 0
        for j in range(n - 1, -1, -1):
            maxHeights[j].append(currMax)
            currMax = max(currMax, height[j])

        for i in range(n):
            currWater = min(maxHeights[i]) - height[i]
            if currWater > 0:
                water += min(maxHeights[i]) - height[i]

        return water
