class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currBuy = float('inf')

        for price in prices:
            if price > currBuy:
                maxProfit += price - currBuy
                currBuy = price

            currBuy = min(currBuy, price)

        return maxProfit
