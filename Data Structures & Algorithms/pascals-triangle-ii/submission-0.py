class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 1:
            return [1]

        prev = [1, 1]

        for i in range(2, rowIndex + 1):
            curr = [0] * (i + 1)
            for j in range(len(curr)):
                if j == 0:
                    curr[j] = prev [j]
                elif j == len(curr) - 1:
                    curr[j] = prev[-1]
                else:
                    curr[j] = prev[j - 1] + prev[j]
            prev = curr

        return prev
