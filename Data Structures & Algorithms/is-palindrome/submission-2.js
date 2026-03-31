class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0 
        let r = s.length - 1

        while (l <= r) {
            const isLeftAlphaNum = this.isAlphanumeric(s[l])
            const isRightAlphaNum = this.isAlphanumeric(s[r])

            if (isLeftAlphaNum && isRightAlphaNum) {
                if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                    return false
                } else {
                    l++
                    r--
                }
            } if (!isLeftAlphaNum) {
                l++
            } if (!isRightAlphaNum) {
                r--
            }
        }
        return true
    }

    isAlphanumeric(c) {
        return /^[a-zA-Z0-9]+$/.test(c)
    }
}
