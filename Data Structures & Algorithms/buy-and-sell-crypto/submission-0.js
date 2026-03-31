class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        const n = prices.length
        let max_profit = 0

        if (n == 1){
            return max_profit
        }

        let i = 0;
        let j = 1;
        while (j < prices.length){
            if (prices[j] < prices[i]){
                i = j
            } else {
                const current_profit = prices[j] - prices[i]
                if (current_profit > max_profit){
                    max_profit = current_profit
                }
                j++
            }
        }

        return max_profit
    }
}
