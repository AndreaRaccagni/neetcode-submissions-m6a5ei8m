class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s: string, t: string): string {
        if (t.length > s.length) return ''

        const sMap: Record<string, number> = {}
        const tMap: Record<string, number> = {}

        for (const c of t) {
            tMap[c] = (tMap[c] ?? 0) + 1
        }

        let l = 0
        let minLength = Infinity
        let res: [number, number] = [-1, -1]

        for (let r = 0; r < s.length; r++) {
            sMap[s[r]] = (sMap[s[r]] ?? 0) + 1

            while (this.checkIfSubstring(sMap, tMap)) {
                const currLength = r - l + 1

                if (currLength < minLength) {
                    minLength = currLength
                    res = [l, r]
                }

                sMap[s[l]]--
                l++
            }
        }

        if (res[0] === -1) return ''

        return s.slice(res[0], res[1] + 1)
    }

    checkIfSubstring(
        map1: Record<string, number>,
        map2: Record<string, number>
    ): boolean {
        for (const c of Object.keys(map2)) {
            if ((map1[c] ?? 0) < map2[c]) {
                return false
            }
        }

        return true
    }
}