class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.reduce((acc, curr) => acc += `${curr.length}#${curr}`, '')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let wordLen = ''
        const decoded = []
        let i = 0

        while (i < str.length) {
            if (str[i] !== '#') {
                wordLen += str[i]
                i++
                continue
            }

            const start = i + 1
            const end = start + parseInt(wordLen)
            decoded.push(str.slice(start, end))
            wordLen = ''
            i = end
        }
        return decoded
    }
}
