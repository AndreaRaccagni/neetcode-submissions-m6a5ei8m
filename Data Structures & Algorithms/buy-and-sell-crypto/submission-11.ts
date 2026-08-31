class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let minPrice = Infinity
        let maxProfit = 0

        for (const p of prices) {
            maxProfit = Math.max(maxProfit, p - minPrice)
            minPrice = Math.min(minPrice, p)
        }

        return maxProfit
    }
}
