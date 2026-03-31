class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r < len(nums):
            if nums[r] <= nums[l]:
                r += 1
                continue
            l += 1

            nums[r], nums[l] = nums[l], nums[r]
            
        return l + 1