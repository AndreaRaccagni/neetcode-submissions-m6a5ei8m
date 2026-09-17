class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]

        for i in range(2, len(cost)):
            one, two = two, min(one, two) + cost[i]

        return min(one, two)