class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const map = {};
        let l = 0;
        let result = 0;
        let currMax = 0;

        for (let r = 0, n = s.length; r < n; r++) {
            map[s[r]] = (map[s[r]] || 0) + 1;
            currMax = Math.max(currMax, map[s[r]])

            while (r - l + 1  - currMax > k) {
                map[s[l]] -= 1;
                l++;
            }
            result = Math.max(r - l + 1, result)
        }
        return result
    }
}
