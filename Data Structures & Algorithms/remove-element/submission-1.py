class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                if nums[r] == val:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1    
        return l
