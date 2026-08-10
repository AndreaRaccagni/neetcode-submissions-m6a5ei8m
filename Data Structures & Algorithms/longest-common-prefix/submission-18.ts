class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs: string[]): string {
        let prefix = strs[0]

        for (const s of strs) {
            prefix = this.findCommonPrefix(prefix, s)
        }
        return prefix
    }

    findCommonPrefix(w1: string, w2: string) {
        let p = 0
        while (p < w1.length && p < w2.length) {
            if (w1[p] !== w2[p]) {
                return w1.slice(0, p)
            }
            p++
        }
        return w1.slice(0, p)
    }
}
