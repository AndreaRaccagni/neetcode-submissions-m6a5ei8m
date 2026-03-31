class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        nums_set = set(nums)
        return len(nums_set) != len(nums)