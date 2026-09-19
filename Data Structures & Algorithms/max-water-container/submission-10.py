class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = (r - l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            currArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, currArea)

        return maxArea
