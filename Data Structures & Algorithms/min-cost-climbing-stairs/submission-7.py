class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0

        for c in cost:
            one, two = two, min(one, two) + c

        return min(one, two)