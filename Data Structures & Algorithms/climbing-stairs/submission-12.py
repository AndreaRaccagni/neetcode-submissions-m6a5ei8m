class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        curr = 2
        prev = 1

        for _ in range(2, n):
            curr, prev = prev + curr, curr

        return curr