class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        generated = set()

        def generateSubsets(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            generateSubsets(i + 1, curr)
            curr.pop()
            
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            generateSubsets(i + 1, curr)
        

        generateSubsets(0, [])
        return res