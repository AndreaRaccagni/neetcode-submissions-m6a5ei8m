class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            curr = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm[:]
                    new_perm.insert(i, n)
                    curr.append(new_perm)
            res = curr

        return res