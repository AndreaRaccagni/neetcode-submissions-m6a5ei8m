/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        const n = pairs.length
        const res = []

        for (let i = 0; i < n; i++) {
            const tmp = pairs[i]
            let j = i - 1
            
            while (j >= 0 && tmp.key < pairs[j].key) {
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j--;
            }
            res.push([...pairs]);
            
        }
        return res;
    }
}
