class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost: number[]): number {
        let one = cost[0]
        let two = cost[1]

        for (let i = 2; i < cost.length; i++) {
            [one, two] = [two, Math.min(one, two) + cost[i]]
        }

        return Math.min(one, two)
    }
}
