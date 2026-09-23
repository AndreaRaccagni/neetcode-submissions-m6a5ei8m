class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            rate = l + (r - l) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / rate)

            if hrs <= h:
                r = rate - 1
            else:
                l = rate + 1

        return l