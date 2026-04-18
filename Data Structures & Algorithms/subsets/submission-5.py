class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generateSet(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            generateSet(i + 1, curr)

            curr.pop()
            generateSet(i + 1, curr)

        generateSet(0, [])
        return res