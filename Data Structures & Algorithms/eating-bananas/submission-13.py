class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r - l) // 2

            k = 0
            for pile in piles:
                k += math.ceil(pile / mid)

            if k > h:
                l = mid + 1
            else:
                r = mid

        return l
