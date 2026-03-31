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
        const n = pairs.length;
        const res = []; // To store the intermediate states of the array

        for (let i = 0; i < n; i++) {
            let j = i - 1;

            // Move elements that are greater than key one position ahead
            while (j >= 0 && pairs[j].key > pairs[j + 1].key) {
                [pairs[j], pairs[j + 1]] = [pairs[j + 1], pairs[j]];
                j -= 1;
            }

            // Clone and save the entire state of the array at this point
            res.push([...pairs]);
        }

        return res;
    }
}
