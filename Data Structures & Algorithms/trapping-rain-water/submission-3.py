class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_bounds = [0] * n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, height[i])
            left_bounds[i] = curr_max

        right_bounds = [0] * n
        curr_max = 0
        for j in range(n - 1, -1, -1):
            curr_max = max(curr_max, height[j])
            right_bounds[j] = curr_max

        total_water = 0
        for k in range(n):
            water = min(left_bounds[k], right_bounds[k]) - height[k]
            total_water += water if water > 0 else 0

        return total_water