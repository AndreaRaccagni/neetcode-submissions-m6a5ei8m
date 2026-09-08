class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s: string, t: string): string {
        if (t.length > s.length) {
            return ''
        }

        const mapS = {}
        const mapT = {}

        for (let i = 0; i < t.length; i++) {
            mapT[t[i]] = (mapT[t[i]] || 0) + 1 
        }

        let have = 0
        const need = Object.keys(mapT).length
        let l = 0
        let res = [-1, -1]
        let minLen = Infinity

        for (let r = 0; r < s.length; r++) {
            const c = s[r]
            mapS[c] = (mapS[c] || 0) + 1

            if (mapS[c] === mapT[c]) {
                have++
            }

            while (have === need) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1
                    res = [l, r]
                }
                mapS[s[l]]--

                if (mapS[s[l]] < mapT[s[l]]) {
                    have--
                }
                l++
            }
        }

        if (res[0] === -1) return ''
        return s.slice(res[0], res[1] + 1)
    }
}
