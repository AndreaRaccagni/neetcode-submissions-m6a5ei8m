class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    validPalindrome(s: string): boolean {
        let l = 0
        let r = s.length - 1
        while (l < r) {
            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return this.isPalindrome(s.slice(l, r)) || this.isPalindrome(s.slice(l + 1, r + 1))
            }
            l++
            r--
        }
        return true
    }

    isPalindrome(s: string): boolean {
        let l = 0
        let r = s.length - 1
        while (l < r) {
            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false
            }
            l++
            r--
        }
        return true
    }
}
