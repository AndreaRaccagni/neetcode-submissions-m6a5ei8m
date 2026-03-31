class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        currMax = nums[0]

        while r < len(nums):
            if nums[r] > currMax:
                currMax = nums[r]
                l += 1
                nums[l] = nums[r]
            
            r += 1
        
        return l + 1