class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1
        let r = Math.max(...piles)

        console.log(l, r)

        while (l < r) {
            const mid = Math.floor((r - l) / 2) + l

            let k = 0
            for (const pile of piles) {
                k += Math.ceil(pile / mid)
            }

            console.log(k)

            if (k > h) {
                l = mid + 1
            } else {
                r = mid
            }
        }

        return l

    }
}
