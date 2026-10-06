class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        one, two = 0, 0
        for i in range(len(nums)):
            one, two = max(one, two), max(one + nums[i], two)

        return max(one, two)
