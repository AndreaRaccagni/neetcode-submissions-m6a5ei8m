class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            minHeight = float('inf')
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                area = minHeight * (j - i + 1)
                maxArea = max(area, maxArea)

        return maxArea