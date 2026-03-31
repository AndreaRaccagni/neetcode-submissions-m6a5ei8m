class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = ''
        for (const str of strs){
            encoded += `${str.length}#${str}`
        }
        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 1;
        let j = 0;
        const decoded = [];

        while (i < str.length) {
            if (str[i] !== '#') {
                i++;
                continue;
            } 

            const wordLen = parseInt(str.slice(j, i));
            decoded.push(str.slice(i + 1, i + wordLen + 1));
            j = i + wordLen + 1;
            i = j + 1;
        }

        return decoded
    }
}
