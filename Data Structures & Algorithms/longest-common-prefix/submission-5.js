class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        const prefixMap = strs[0].split('');

        for (const str of strs) {
            if (!str) return ''
            if (str.length < prefixMap.length) {
                prefixMap[str.length] = null;
            }

            let j = 0;
            while (j < str.length && j < prefixMap.length && prefixMap[j]) {
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
