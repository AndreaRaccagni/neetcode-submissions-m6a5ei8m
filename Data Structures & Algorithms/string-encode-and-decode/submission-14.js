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
        if (!str) return []

        let wordLen = 0
        const decoded = []
        let i = 0

        while (i < str.length) {
            if (str[i] === '#') {
                const start = i + 1
                const end = start + parseInt(wordLen)
                decoded.push(str.slice(start, end))
                wordLen = ''
                i = end
            } else {
                wordLen += str[i]
                i++
            }
        }
        return decoded
    }
}
