class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (r - l) // 2 + l
            k = self.hoursToEatBananas(piles, mid)

            if k > h:
                l = mid + 1
            else:
                r = mid - 1

        return l
    
    def hoursToEatBananas(self, piles, rate):
        hours = 0
        for p in piles:
            hours += math.ceil(p / rate)

        return hours