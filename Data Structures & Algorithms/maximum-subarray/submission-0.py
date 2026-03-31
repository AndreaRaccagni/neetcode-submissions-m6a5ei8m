class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                l = r
                currSum = 0
        
        return maxSum