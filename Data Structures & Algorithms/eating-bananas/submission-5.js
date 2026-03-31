class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1;
        let r = Math.max(...piles)
        let result = r

        while (l <= r) {
            const k = Math.round((r + l) / 2)
            let total = 0

            for (const pile of piles) {
                total += Math.ceil(pile / k)
            }

            if (total > h) {
                l = k + 1
            } else {
                result = k
                r = k - 1
            }
        }

        return result
    }
}
