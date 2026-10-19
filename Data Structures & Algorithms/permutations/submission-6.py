class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for n in nums:
            res = []
            for perm in output:
                for i in range(0, len(perm) + 1):
                    perm.insert(i, n)
                    res.append(perm[:])
                    perm.pop(i)
            
            output = res
        return output