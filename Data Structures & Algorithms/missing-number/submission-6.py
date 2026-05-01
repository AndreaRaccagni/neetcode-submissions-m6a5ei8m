class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + [n + 1]
        zero = False

        for i in range(n):
            index = abs(nums[i])
            if nums[index] == 0:
                zero = True
            else:
                nums[index] *= -1

        print(nums)

        for i in range(n + 1):
            if nums[i] > 0 or nums[i] == 0 and not zero:
                return i

