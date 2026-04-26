class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        currProd = 1

        for n in nums:
            res.append(currProd)
            currProd *= n

        currProd = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= currProd
            currProd *= nums[i]

        return res