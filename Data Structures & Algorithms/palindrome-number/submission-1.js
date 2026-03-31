class Solution {
    /**
     * @param {number} x
     * @return {boolean}
     */
    isPalindrome(x) {
        const n = Number(x).toString();
        let l = 0;
        let r = n.length - 1;

        while (l < r) {
            if (n[l] !== n[r]) {
                return false;
            }
            r--
            l++;
        }

        return true;
    }
}
