class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        prev = nums[0]
        curr = nums[1]

        for i in range(2, len(nums)):
            prev, curr = max(prev, curr), max(curr, prev + nums[i])

        return curr