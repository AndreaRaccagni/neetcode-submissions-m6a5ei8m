class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def createCombination(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            createCombination(i, curr, total + nums[i])

            curr.pop()
            createCombination(i + 1, curr, total)

        createCombination(0, [], 0)
        return res






