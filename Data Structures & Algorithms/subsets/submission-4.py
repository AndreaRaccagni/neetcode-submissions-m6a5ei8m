class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def createSubsets(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            createSubsets(i + 1, curr)

            curr.pop()
            createSubsets(i + 1, curr)

        createSubsets(0, [])
        return res