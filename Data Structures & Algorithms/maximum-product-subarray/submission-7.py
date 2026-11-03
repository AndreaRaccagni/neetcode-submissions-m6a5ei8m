class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_product = 1
        max_product = float('-inf')

        for n in nums:
            curr_product *= n
            max_product = max(max_product, curr_product)

            if curr_product == 0:
                curr_product = 1

        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_product *= nums[i]
            max_product = max(max_product, curr_product)

            if curr_product == 0:
                curr_product = 1

        return max_product