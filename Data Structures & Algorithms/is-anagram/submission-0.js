class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sSorted = s.split('').sort((a, b) => a.localeCompare(b)).join('')
        const tSorted = t.split('').sort((a, b) => a.localeCompare(b)).join('')

        return sSorted === tSorted
    }
}
