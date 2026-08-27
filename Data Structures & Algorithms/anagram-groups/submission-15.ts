class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const hashMap: Record<string, string[]> = {}

        for (const s of strs) {
            const hashKey = this.createHash(s)

            if (hashMap[hashKey]) {
                hashMap[hashKey].push(s)
            } else {
                hashMap[hashKey] = [s]
            }
        }

        return Object.values(hashMap)

    }

    createHash(s: string): string {
        const abc = new Array(26).fill(0)
        const shift = 'a'.charCodeAt(0)

        for (let i = 0; i < s.length; i++) {
            abc[s[i].charCodeAt(0) - shift] += 1
        }

        return abc.join('#')
    }
}
