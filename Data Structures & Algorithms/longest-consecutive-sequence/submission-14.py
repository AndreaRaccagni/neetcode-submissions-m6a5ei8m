class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        maxConsecutive = 0

        for num in nums:
            count = 0
            curr = num
            if curr - 1 not in hashNums:
                while curr in hashNums:
                    count += 1
                    curr += 1
                maxConsecutive = max(maxConsecutive, count)

        return maxConsecutive
            