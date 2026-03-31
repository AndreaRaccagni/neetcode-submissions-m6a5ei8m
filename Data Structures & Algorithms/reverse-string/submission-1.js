class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        const n = s.length - 1;
        let i = 0;

        while (i < n / 2) {
            [s[i], s[n - i]] = [s[n - i], s[i]]
            i++;
        }

        return s
    }
}
