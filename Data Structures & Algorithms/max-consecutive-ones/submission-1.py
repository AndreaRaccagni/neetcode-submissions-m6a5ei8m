class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currCount = 0

        for n in nums:
            if n != 1:
                currCount = 0
            else:
                currCount += 1
                
            maxCount = max(maxCount, currCount)

        return maxCount
