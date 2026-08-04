class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]

        for c in cost[2:]:
            one, two = two, c + min(two, one)

        return min(one, two)