class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, curr = 0, 0
        for i in range(len(nums) - 1):
            prev, curr = curr, max(curr, prev + nums[i])

        prev1, curr1 = 0, 0
        for j in range(1, len(nums)):
            prev1, curr1 = curr1, max(curr1, prev1 + nums[j])

        return max(curr, curr1)