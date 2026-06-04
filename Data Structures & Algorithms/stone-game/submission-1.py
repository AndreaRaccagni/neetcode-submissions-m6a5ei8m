class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = 0
        r = len(piles) - 1
        alice = 0
        bob = 0

        while l < r:
            alice += max(piles[l], piles[r])
            bob += min(piles[l], piles[r])
            l += 1
            r -= 1

        return alice > bob
