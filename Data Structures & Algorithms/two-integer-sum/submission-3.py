class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            if num in num_map:
                return [num_map[num], i]
            else:
                num_map[target - num] = i
        
        return []