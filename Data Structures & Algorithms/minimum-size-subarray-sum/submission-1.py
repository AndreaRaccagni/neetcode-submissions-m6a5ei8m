class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums) + 1
        currSum = 0
        l = 0

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1

        return 0 if minLen == len(nums) + 1 else minLen