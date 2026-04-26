class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        maxLength = 0

        for n in hashNums:
            if n - 1 in hashNums:
                continue

            start = n
            currLength = 1
            
            while start + 1 in hashNums:
                currLength += 1
                start += 1

            maxLength = max(currLength, maxLength)

        return maxLength
