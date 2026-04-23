class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def generateCombinations(i, curr):
            if i > n:
                if len(curr) == k:
                    res.append(curr[:])
                return

            curr.append(i)
            generateCombinations(i + 1, curr)

            curr.pop()
            generateCombinations(i + 1, curr)

        generateCombinations(1, [])
        
        return res