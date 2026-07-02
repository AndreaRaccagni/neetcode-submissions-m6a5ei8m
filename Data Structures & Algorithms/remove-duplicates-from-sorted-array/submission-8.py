class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0

        for n in nums:
            if n != nums[p]:
                p += 1
                nums[p] = n

        return p + 1