class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        old = 0
        new = 0

        for c in cost:
            old, new = new, min(old, new) + c

        return min(old, new)