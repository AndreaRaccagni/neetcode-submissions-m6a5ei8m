class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 0

        while r < len(prices) - 1:
            r += 1
            curr_profit = prices[r] - prices[l]
            profit = max(curr_profit, profit)

            if prices[r] < prices[l]:
                l = r
            
        return profit

