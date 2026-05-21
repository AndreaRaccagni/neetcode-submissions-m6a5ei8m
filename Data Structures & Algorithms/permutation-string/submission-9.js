class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) return false

        const window = s1.length

        const map1 = new Array(26).fill(0)
        const map2 = new Array(26).fill(0)

        for (let i = 0; i < window; i++) {
            map1[s1[i].charCodeAt(0) - "a".charCodeAt(0)]++
            map2[s2[i].charCodeAt(0) - "a".charCodeAt(0)]++
        }
        
        let count = 0
        for (let i = 0; i < map1.length; i++) {
            if (map1[i] === map2[i]) {
                count++
            }
        }
        
        for (let i = window; i < s2.length; i++) {
            if (count === 26) {
                return true
            }


            const r_index = s2[i].charCodeAt(0) - "a".charCodeAt(0)
            map2[r_index]++
            if (map1[r_index] === map2[r_index]) {
                count++
            } else if (map1[r_index] === map2[r_index] - 1) {
                count--
            }

            const l_index = s2[i - window].charCodeAt(0) - "a".charCodeAt(0)
            map2[l_index]--
            if (map1[l_index] === map2[l_index]) {
                count++
            } else if (map1[l_index] === map2[l_index] + 1) {
                count--
            }

        }

        return count === 26
    }
}
