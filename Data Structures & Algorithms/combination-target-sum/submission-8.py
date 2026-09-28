class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(curr, i, total):
            if total == target:
                res.append(curr[:])
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            backtracking(curr, i, total + nums[i])
            
            curr.pop()
            backtracking(curr, i + 1, total)

        backtracking([], 0, 0)

        return res