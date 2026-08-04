class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        one = nums[0]
        two = nums[1]

        for i in range(2, len(nums)):
            one, two = max(one, two), max(two, one + nums[i])

        return max(one, two)