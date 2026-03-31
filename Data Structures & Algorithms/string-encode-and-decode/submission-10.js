class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(!strs.length) return '0.0'
        return strs.join('0.0')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str === '0.0') return []
        return str.split('0.0')
    }
}
