class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums) - 1:
            if nums[i + 1] != nums[i]:
                i += 1
            else:
                nums.pop(i + 1)
        
        return i + 1