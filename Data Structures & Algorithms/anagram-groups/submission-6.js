class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupedAnagrams = {}

        for (const str of strs){
            const mapStr = new Array(26).fill(0)

            for (const c of str){
                const i = c.charCodeAt() - 'a'.charCodeAt()
                mapStr[i] += 1
            }

            const strHash = mapStr.join('*')

            if(!groupedAnagrams[strHash]){
                groupedAnagrams[strHash] = []
            }
            groupedAnagrams[strHash].push(str)
        }

        return Object.values(groupedAnagrams)
    }
}       
