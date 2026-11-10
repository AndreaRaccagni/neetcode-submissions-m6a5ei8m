class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false

        const charCount = Array.from({length: 26}, () => 0)
        for (let i = 0; i < s.length; i++) {
            const sIndex = s[i].charCodeAt(0) - 'a'.charCodeAt(0)
            const tIndex = t[i].charCodeAt(0) - 'a'.charCodeAt(0)
            charCount[sIndex]++
            charCount[tIndex]--
        }

        for (const n of charCount) {
            if (n !== 0) return false
        }
        return true
    }
}
