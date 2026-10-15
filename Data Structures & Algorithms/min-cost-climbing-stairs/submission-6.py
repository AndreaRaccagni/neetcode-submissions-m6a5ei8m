class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        curr = 0

        for i in range(len(cost)):
            prev, curr = curr, min(curr, prev) + cost[i]

        return min(curr, prev)