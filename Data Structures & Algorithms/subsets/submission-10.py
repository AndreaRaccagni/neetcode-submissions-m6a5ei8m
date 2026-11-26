class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()
            backtracking(i + 1, curr)
            
        backtracking(0, [])
        return res