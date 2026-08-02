class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        prev = 1
        curr = 2

        for i in range(2, n):
            curr, prev = curr + prev, curr

        return curr