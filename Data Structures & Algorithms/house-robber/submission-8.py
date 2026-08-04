class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        one = nums[0]
        two = nums[1]

        for i in range(2, len(nums)):
            one, two = max(one, two), max(two, one + nums[i])

        return max(one, two)