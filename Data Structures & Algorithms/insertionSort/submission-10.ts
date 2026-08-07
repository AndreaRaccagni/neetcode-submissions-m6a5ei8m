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
    insertionSort(pairs: Pair[]): Pair[][] {
        const res = []
        for (let i = 0; i < pairs.length; i++) {
            for (let j = i; j > 0; j--) {
                if (pairs[j].key < pairs[j - 1].key) {
                    [pairs[j], pairs[j - 1]] = [pairs[j - 1], pairs[j]]
                }
            }
            res.push([...pairs]);
        }
        return res
    }
}
