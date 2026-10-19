class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for n in nums:
            res = []
            for perm in output:
                for i in range(len(perm) + 1):
                    new_perm = perm[:]
                    new_perm.insert(i, n)
                    res.append(new_perm)           
            output = res
        return output