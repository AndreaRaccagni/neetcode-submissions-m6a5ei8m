class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        left = 0
        right = 0

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        left = l
                        right = r
                    l -= 1
                    r += 1
                else:
                    break

        for i in range(len(s)):
            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        left = l
                        right = r
                    l -= 1
                    r += 1
                else:
                    break
        
        return s[left : right + 1]