class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def combine(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return

            if i == len(nums) or total > target:
                return

            curr.append(nums[i])
            combine(i, curr, total + nums[i]) 
            curr.pop()
            combine(i + 1, curr, total)

        combine(0, [], 0)
        return result