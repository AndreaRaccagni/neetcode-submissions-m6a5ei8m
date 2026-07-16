class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let res = ''
        for (const s of strs) {
            res += `${s.length}#${s}`
        }

        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const res: string[] = []
        let l = 0
        let r = 0

        while (l < str.length) {
            if (str[r] == '#') {
                const len = Number(str.slice(l, r))
                const word = str.slice(r + 1, r + len + 1)
                res.push(word)
                l = r + len + 1
                r += len + 1
            } else {
                r += 1
            }
        }

        return res
    }
}
