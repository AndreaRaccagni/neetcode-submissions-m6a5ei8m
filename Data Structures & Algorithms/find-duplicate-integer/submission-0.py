class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = [1 for x in range(len(nums) + 1)]

        print(num_count)

        for num in nums:
            num_count[num] -= 1
            if num_count[num] < 0:
                return num