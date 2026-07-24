class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = 0

        for i in range(2):
            total += prices[i]

        return money - total if money - total >= 0 else money