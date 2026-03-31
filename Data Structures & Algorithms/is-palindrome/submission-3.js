class Solution {
    isPalindrome(s) {
        let l = 0, r = s.length - 1

        while (l < r) {
            while (l < r && !this.isAlphaNum(s[l])) l++
            while (l < r && !this.isAlphaNum(s[r])) r--

            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false
            }

            l++
            r--
        }

        return true
    }

    isAlphaNum(c) {
        return c.toLowerCase() !== c.toUpperCase() || (c >= '0' && c <= '9')
    }
}