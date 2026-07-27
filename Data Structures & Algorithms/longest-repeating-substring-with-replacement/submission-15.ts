class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        const inWindow = {}
        let l = 0
        let maxLen = 0
        let maxChar = 0

        for (let r = 0; r < s.length; r++) {
            inWindow[s[r]] = (inWindow[s[r]] || 0) + 1
            maxChar = Math.max(inWindow[s[r]], maxChar)

            while (maxChar + k < r - l + 1) {
                inWindow[s[l]] -= 1
                l +=1
            }
            maxLen = Math.max(maxLen, r - l + 1)
        }
        return maxLen
    }
}
