class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0

        for i in range(len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)

        return max(prev, curr)