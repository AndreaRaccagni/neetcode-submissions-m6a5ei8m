class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        left_height = height[l]
        right_height = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                left_height = max(left_height, height[l])
                water += left_height - height[l]
            else:
                r -= 1
                right_height = max(right_height, height[r])
                water += right_height - height[r]
        
        return water


