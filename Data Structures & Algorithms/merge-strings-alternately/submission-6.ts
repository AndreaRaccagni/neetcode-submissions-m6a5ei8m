class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1: string, word2: string): string {
        let p = 0
        let q = 0
        const res = []

        while (p < word1.length || q < word2.length) {
            const c1 = p < word1.length ? word1[p] : ''
            res.push(c1)
            p++

            const c2 = q < word2.length ? word2[q] : ''
            res.push(c2)
            q++
        }

        return res.join('')
    }
}
