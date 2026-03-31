class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let shortestIndex = 0;

        for (let i = 0; i < strs.length; i++) {
            if (strs[i].length < strs[shortestIndex].length) {
                shortestIndex = i;
            }
        }

        const prefixMap = strs[shortestIndex].split('');

        for (const str of strs) {
            if (!str) return ''

            let j = 0;
            while (j < prefixMap.length && prefixMap[j]) {
                if (str[j] !== prefixMap[j]) {
                    prefixMap[j] = null;
                    break;
                }
                j++;
            }

        }


        let prefix = ''
        for (const c of prefixMap) {
            if (!c) {
                break;
            }
            prefix += c
        }
        return prefix;
    }
}
