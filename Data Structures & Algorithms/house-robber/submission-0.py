class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                houses[i] = nums[i]
                continue
            elif i == 1:
                houses[i] = max(nums[i], nums[i - 1])
            else:
                houses[i] = max(nums[i] + houses[i - 2], houses[i - 1])

        return houses[-1]
            
