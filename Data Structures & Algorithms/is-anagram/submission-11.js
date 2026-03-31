class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false

        const sMap = {}
        const tMap = {}

        for (let i = 0; i < s.length; i++){
            sMap[s[i]] = (sMap[s[i]] || 0) + 1
            tMap[t[i]] = (tMap[t[i]] || 0) + 1
        }

        for (const char in sMap){
            if (sMap[char] !== tMap[char]){
                return false
            }
        }

        return true

    }
}
