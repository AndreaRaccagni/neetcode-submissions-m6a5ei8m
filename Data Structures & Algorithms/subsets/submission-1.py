class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def createComninations(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            createComninations(i + 1)

            curr.pop()
            createComninations(i + 1)

        createComninations(0)
        return res