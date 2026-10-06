class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        one = 0
        two = 0
        for i in range(len(nums) - 1):
            one, two = max(one, two), max(one + nums[i], two)

        even = max(one, two)

        one = 0
        two = 0
        for i in range(1, len(nums)):
            one, two = max(one, two), max(one + nums[i], two)
        
        odd = max(one, two)

        return max(even, odd)