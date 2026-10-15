class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float('-inf')
        currProd = 1

        for i in range(len(nums)):
            currProd *= nums[i]
            maxProd = max(currProd, maxProd)
            if currProd == 0:
                currProd = 1
                
        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            currProd *= nums[i]
            maxProd = max(currProd, maxProd)
            if currProd == 0:
                currProd = 1

        return maxProd
        
