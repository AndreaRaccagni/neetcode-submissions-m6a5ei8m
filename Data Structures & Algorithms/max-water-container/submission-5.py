class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area