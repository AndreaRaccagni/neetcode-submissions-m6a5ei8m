class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let l = 0
        let r = s.length - 1

        while (l < r) {
            if (!this.isAlphaNum(s[l])) {
                l++
            } else if (!this.isAlphaNum(s[r])) {
                r--
            } else {
                if (s[l].toLowerCase() != s[r].toLowerCase()) {
                    return false
                }
                l++
                r--
            }
        }
        return true
    }


    isAlphaNum(c: string): boolean {

        const code = c.charCodeAt(0)
        return (
            (code >= 48 && code <= 57) ||
            (code >= 65 && code <= 90) || 
            (code >= 97 && code <= 122)   
        )

    }
}
