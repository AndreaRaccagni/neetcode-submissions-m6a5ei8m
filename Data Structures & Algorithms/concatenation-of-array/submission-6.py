class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = [0] * (n * 2)

        for i in range(n):
            newArr[i] = newArr[i + n] = nums[i]

        return newArr