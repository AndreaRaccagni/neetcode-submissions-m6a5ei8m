class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for p in prices:
            maxProfit = max(maxProfit, p - minBuy)
            minBuy = min(minBuy, p)

        return maxProfit