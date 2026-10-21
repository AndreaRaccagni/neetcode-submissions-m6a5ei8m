class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            curr = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    new_perm = perm[:]
                    new_perm.insert(i, n)
                    curr.append(new_perm)
            
            permutations = curr

        return permutations