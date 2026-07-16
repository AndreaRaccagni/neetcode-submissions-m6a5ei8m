class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false

        const abc: number[] = new Array(26).fill(0)
        const offset = 'a'.charCodeAt(0)

        for (let i = 0; i < s.length; i++) {
            abc[s[i].charCodeAt(0) - offset] += 1
            abc[t[i].charCodeAt(0) - offset] -= 1
        }

        for (const c of abc) {
            if (c !== 0) {
                return false
            }
        }

        return true
    }
}
