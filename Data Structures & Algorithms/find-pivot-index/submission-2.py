class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        currSum = 0

        for i in range(len(nums)):
            if currSum * 2 == total - nums[i]:
                return i

            currSum += nums[i]

        return -1