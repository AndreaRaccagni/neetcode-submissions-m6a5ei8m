class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNum = {}
        
        for num in nums:
            countNum[num] = 1 + countNum.get(num, 0)
            
            if countNum[num] > len(nums) / 2:
                return num