class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0

        while l <= r:
            mid = (r - l) // 2 + l
            product = mid * mid

            if product < x:
                l = mid + 1
                res = mid
            elif product > x:
                r = mid - 1
            else:
                return mid

        return res
