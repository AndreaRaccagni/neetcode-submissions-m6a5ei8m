class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        max_len = 0
        l = 0
        r = 0

        for i in range(len(s)):
            odd = self.findLongestPalindrome(s, i, i)
            even = self.findLongestPalindrome(s, i, i + 1)

            best = odd if odd['size'] > even['size'] else even
            print(best)

            if max_len < best['size']:
                max_len = best['size']
                l = best['l']
                r = best['r']

        return s[l:r + 1]


    def findLongestPalindrome(self, s, i, j):
        l = i
        r = j

        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return {
            'l': l + 1,
            'r': r - 1,
            'size': (r - 1) - (l + 1) + 1
        }
            

        

                