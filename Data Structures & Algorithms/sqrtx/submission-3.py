class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            mid = (r - l) // 2 + l
            power = mid * mid

            if power > x:
                r = mid - 1
            elif power < x:
                l = mid + 1
                res = mid
            else:
                return mid

        return res