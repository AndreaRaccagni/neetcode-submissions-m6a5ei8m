class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        expected = ((len(nums)) * (len(nums) + 1)) / 2 

        return int(expected - total)
            