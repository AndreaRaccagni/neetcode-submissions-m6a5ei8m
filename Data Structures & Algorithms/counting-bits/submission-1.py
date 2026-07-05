class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for n in range(n + 1):
            count = 0
            for i in range(32):
                count += n & 1
                n = n >> 1

            res.append(count)

        return res