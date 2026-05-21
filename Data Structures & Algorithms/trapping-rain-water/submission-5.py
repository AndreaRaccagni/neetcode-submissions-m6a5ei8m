class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_height = height[l]
        right_height = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                left_height = max(left_height, height[l])
                bound = min(left_height, right_height)
                water += bound - height[l] if bound - height[l] > 0 else 0
            else:
                r -= 1
                right_height = max(right_height, height[r])
                bound = min(left_height, right_height)
                water += bound - height[r] if bound - height[r] > 0 else 0
        
        return water


