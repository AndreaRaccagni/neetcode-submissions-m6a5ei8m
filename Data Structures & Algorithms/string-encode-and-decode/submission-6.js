class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (!strs.length) return null

        let encoded = ''
        for (let word of strs){
            encoded += `${word.length}#${word}`
        }

        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str === null) return []

        let decoded = [] 
        let start = 0
        let i = 0

        while (i < str.length){
            if (str[i] === '#') {
                const len = parseInt(str.substring(start, i))
                decoded.push(str.substring(i + 1, i + 1 + len))
                start = i + 1 + len
                i = start + 1
            } else{
                i++
            }
        }

        return decoded
    }

}
