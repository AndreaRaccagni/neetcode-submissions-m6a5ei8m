/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    mergeSort(pairs: Pair[]): Pair[] {
        if (pairs.length <= 1) {
            return pairs
        }

        const mid = Math.floor((pairs.length - 0) / 2)     
        const left = this.mergeSort(pairs.slice(0, mid))
        const right = this.mergeSort(pairs.slice(mid))

        return this.merge(left, right)
    }

    merge(left: Pair[], right: Pair[]): Pair[]  {
        let r = 0
        let l = 0
        let curr = 0
        const size = left.length + right.length
        const merged: Array<Pair | null> = new Array(size).fill(null)

        while (curr < merged.length) {
            const leftVal = l < left.length ? left[l].key: Infinity
            const rightVal = r < right.length ? right[r].key: Infinity

            if (leftVal <= rightVal) {
                merged[curr] = left[l]
                l++
            } else {
                merged[curr] = right[r]
                r++
            }
            curr++
        }

        return merged
    }
}
