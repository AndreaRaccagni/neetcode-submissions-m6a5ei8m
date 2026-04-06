class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        steps = [1, 2]
        for i in range(3, n + 1):
            steps[0], steps[1] = steps[1], steps[0] + steps[1]

        return steps[1]
            

        