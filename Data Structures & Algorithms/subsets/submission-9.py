class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(curr, index):
            if index >= len(nums):
                res.append(curr[:])
                return

            curr.append(nums[index])
            backtracking(curr, index + 1)

            curr.pop()
            backtracking(curr, index + 1)


        backtracking([], 0)
        return res