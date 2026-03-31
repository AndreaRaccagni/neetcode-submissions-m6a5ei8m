class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0
        let maxLen = 0
        const seen = new Set()

        for (let r = 0; r < s.length; r++) {
            while (seen.has(s[r])) {
                seen.delete(s[l])
                l++
            }

            seen.add(s[r])
            maxLen = Math.max(maxLen, r - l + 1)
        }

        return maxLen
    }
}
