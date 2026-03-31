class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagrams = {}
        const baseIndex = 'a'.charCodeAt(0)

        for (const s of strs) {
            const charMap = new Array(26).fill(0)

            for (const c of s) {
                charMap[c.charCodeAt(0) - baseIndex] += 1
            }

            const bucket = charMap.join('###')

            if (!anagrams[bucket]) {
                anagrams[bucket] = []
            }
            anagrams[bucket].push(s)
        }

        return Object.values(anagrams)
    }
}
