class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def generateSubset(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            generateSubset(i + 1, curr)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            generateSubset(i + 1, curr)

        generateSubset(0, [])
        return res


