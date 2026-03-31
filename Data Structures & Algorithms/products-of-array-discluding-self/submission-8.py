class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(len(nums)):
            if i > 0:
                prefix[i] = prefix[i - 1] * nums[i - 1]

        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= curr
            curr *= nums[i]

        return prefix