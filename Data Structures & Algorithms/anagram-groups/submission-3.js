class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const mapStrs = {}
        const alphabet = 'abcdefghijklmnopqrstuvwxyz'
        const len = alphabet.length

        for (const str of strs){
            const mapStr = new Array(len).fill(0)
            
            for(const char of str){
                const charIndex = alphabet.indexOf(char)
                mapStr[charIndex] += 1
            }

            const key = mapStr.join('*');

            if(key in mapStrs) {
                mapStrs[key].push(str)
            } else {
                mapStrs[key] = [str]
            }
        }

        return Object.values(mapStrs)
    }
}
