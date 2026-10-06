class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        robbed = [0] * len(nums) 
        robbed[0] = nums[0]
        robbed[1] = nums[1]

        for i in range(2, len(nums)):
            robbed[i] = max(robbed[i - 1], robbed[i - 2] + nums[i])
            robbed[i - 1] = max(robbed[i - 1], robbed[i - 2])
        return max(robbed[-2], robbed[-1])
