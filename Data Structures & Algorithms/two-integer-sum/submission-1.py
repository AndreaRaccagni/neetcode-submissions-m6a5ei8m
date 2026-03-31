class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       mapper = {}

       for i, num in enumerate(nums):
            if num in mapper:
                return [mapper[num],i]
            else:
                mapper[target - num] = i