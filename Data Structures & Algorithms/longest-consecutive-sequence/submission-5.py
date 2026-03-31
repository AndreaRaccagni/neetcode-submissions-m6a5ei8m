class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                curr = num
                length = 1

                while curr + 1 in numsSet:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest