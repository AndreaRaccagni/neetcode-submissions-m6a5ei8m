class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one = 0
        two = 0
        for i in range(len(nums) - 1):
            one, two = max(one, two), max(one + nums[i], two)

        without_last = max(one, two)

        one = 0
        two = 0
        for i in range(1, len(nums)):
            one, two = max(one, two), max(one + nums[i], two)
        
        with_last = max(one, two)

        return max(without_last, with_last)