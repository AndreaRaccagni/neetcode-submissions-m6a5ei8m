class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        target = 0

        for num in nums:
            target = target ^ num

        return target