class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]

        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] = prod * prefix[i]
            prod *= nums[i]

        return prefix

