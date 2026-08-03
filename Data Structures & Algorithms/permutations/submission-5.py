class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            curr = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new = perm[:]
                    new.insert(i, n)
                    curr.append(new)
                res = curr
        
        return res