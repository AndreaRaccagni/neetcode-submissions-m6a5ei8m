class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        p = 0
        n = len(piles) - 1
        alice = 0
        bob = 0

        while p < n:
            alice += max(piles[p], piles[n - p])
            bob += min(piles[p], piles[n - p])
            p += 1

        return alice > bob
