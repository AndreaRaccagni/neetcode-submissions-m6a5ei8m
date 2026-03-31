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

            if(mapStr in mapStrs) {
                mapStrs[mapStr].push(str)
            } else {
                mapStrs[mapStr] = [str]
            }
        }

        console.log(mapStrs)

        return Object.values(mapStrs)
    }
}
