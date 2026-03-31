class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = [False] * (len(nums) + 1)

        for n in nums:
            seen[n] = True

        for i in range(len(seen)):
            if seen[i] == False:
                return i