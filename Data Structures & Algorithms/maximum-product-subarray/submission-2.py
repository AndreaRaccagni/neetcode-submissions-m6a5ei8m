class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float('-inf')
        currProd = 1

        for n in nums:
            currProd *= n
            maxProd = max(maxProd, currProd)
            if currProd == 0:
                currProd = 1
        
        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            currProd *= nums[i]
            maxProd = max(maxProd, currProd)
            if currProd == 0:
                currProd = 1    

        return maxProd    
