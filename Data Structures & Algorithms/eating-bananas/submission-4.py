class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            k = (r + l) // 2

            total = 0
            for pile in piles:
                total += math.ceil(pile/k)

            if total > h:
                l = k + 1
            else:
                result = k
                r = k - 1

        return result
        