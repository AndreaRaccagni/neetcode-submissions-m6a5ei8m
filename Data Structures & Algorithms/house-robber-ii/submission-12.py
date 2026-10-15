class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev = 0
        curr = 0

        for i in range(len(nums) - 1):
            prev, curr = curr, max(prev + nums[i], curr)

        max_with_first = max(prev, curr)

        prev = 0
        curr = 0

        for i in range(1, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)

        max_without_first = max(prev, curr)

        return max(max_with_first, max_without_first)