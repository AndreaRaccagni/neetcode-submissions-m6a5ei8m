class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]

        for i in range(2, len(cost)):
            one, two = two, cost[i] + min(two, one)

        return min(one, two)