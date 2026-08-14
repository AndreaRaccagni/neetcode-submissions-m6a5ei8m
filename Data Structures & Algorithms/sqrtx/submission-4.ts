class Solution {
    /**
     * @param {number} x
     * @return {number}
     */
    mySqrt(x: number): number {
        let l = 0
        let r = x
        let res = 0


        while (l <= r) {
            const mid = Math.floor((r - l) / 2) + l
            const pow = mid * mid

            if (pow === x) {
                return mid
            } else if (pow < x) {
                l = mid + 1
                res = mid
            } else {
                r = mid - 1
            }
        }
        return res
    }
}
