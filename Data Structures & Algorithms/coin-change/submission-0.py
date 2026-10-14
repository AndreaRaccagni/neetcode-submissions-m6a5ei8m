class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [amount + 1] * (amount + 1)
        changes[0] = 0

        for am in range(1, amount + 1):
            for coin in coins:
                if am >= coin:
                    changes[am] = min(changes[am], 1 + changes[am - coin])

        return changes[amount] if changes[amount] != amount + 1 else -1