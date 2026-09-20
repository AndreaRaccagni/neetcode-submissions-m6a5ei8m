class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftToRight = []
        maxHeight = 0
        for h in height:
            maxHeight = max(maxHeight, h)
            leftToRight.append(maxHeight)
        
        rightToLeft = [0] * n
        maxHeight = 0
        for i in range(n - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            rightToLeft[i] = maxHeight
        
        water = 0
        for i in range(n):
            water += min(leftToRight[i], rightToLeft[i]) - height[i]

        return water