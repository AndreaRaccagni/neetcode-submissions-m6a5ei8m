class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [amount + 1] * (amount + 1)
        changes[0] = 0

        for am in range(1, amount + 1):
            for c in coins:
                if am >= c:
                    changes[am] = min(changes[am], 1 + changes[am - c])

        return changes[amount] if changes[amount] != amount + 1 else -1