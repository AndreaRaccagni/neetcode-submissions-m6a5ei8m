class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(!strs.length) return ''
        if(strs.length === 1 && !strs[0]) return '*'
        return strs.join(' \u2022\ ')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log(str)
        if(!str) return []
        if(str === '*') return ['']
        return str.split(' \u2022\ ')
    }
}
