class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sMap = {}
        const tMap = {}

        for(const char of s){
            sMap[char] = (sMap[char] || 0) + 1
        }

        for(const char of t){
            tMap[char] = (tMap[char] || 0) + 1
        }

        if(Object.keys(sMap).length !== Object.keys(tMap).length) return false

        for(const key in sMap){
            if(sMap[key] !== tMap[key]) return false
        }

        return true
    }
}
