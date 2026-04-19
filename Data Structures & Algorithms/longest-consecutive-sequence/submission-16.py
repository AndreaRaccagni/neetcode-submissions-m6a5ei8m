class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0

        for n in nums:
            if n - 1 not in numsSet:
                count = 1
                curr = n
                while curr + 1 in numsSet:
                    count += 1
                    curr += 1

                maxSeq = max(count, maxSeq)

        return maxSeq