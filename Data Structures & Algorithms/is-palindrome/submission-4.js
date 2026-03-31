class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0
        let r = s.length - 1

        while (l < r) {
            if (!this.isAlphaNum(s[l])) {
                l++
                continue
            }
            if (!this.isAlphaNum(s[r])) {
                r--
                continue
            }

            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false
            }
            l++
            r--
        }

        return true
    }

    isAlphaNum(c) {
        const code = c.charCodeAt(0)
        return (
            (code >= 48 && code <= 57) || 
            (code >= 65 && code <= 90) ||
            (code >= 97 && code <= 122)
        )
    }
}
