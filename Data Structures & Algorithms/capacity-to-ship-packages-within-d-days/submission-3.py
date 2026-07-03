class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        minWeight = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            d = self.computeDays(weights, mid)

            if d > days:
                l = mid + 1
            else:
                r = mid - 1
                minWeight = min(minWeight, mid)

        return minWeight


    def computeDays(self, weights, capacity):
        days = 1
        currWeight = 0

        for w in weights:
            currWeight += w

            if currWeight > capacity:
                days += 1
                currWeight = w 

        return days
