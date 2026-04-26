class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            left = s[l].lower()
            right = s[r].lower()

            if not self.isCharValid(left):
                l += 1
                continue

            if not self.isCharValid(right):
                r -= 1
                continue

            if left != right:
                return False

            r -= 1
            l += 1

        return True

    def isCharValid(self, c):
        return 'a' <= c <= 'z' or '0' <= c <= '9'