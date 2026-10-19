class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        r, l = 0, 0

        while r < len(nums) - 1:
            new_max = 0

            for i in range(l, r + 1):
                new_max = max(new_max, i + nums[i])
            l = r + 1
            r = new_max
            jumps += 1

        return jumps