class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        product = 1
        for i in range(len(nums) - 1, - 1, -1):
            res[i] *= product
            product *= nums[i]

        return res

        