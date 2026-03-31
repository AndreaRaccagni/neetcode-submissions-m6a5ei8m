class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            h = min(heights[l], heights[r])
            currArea = h * (r - l)
            area = max(currArea, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return area