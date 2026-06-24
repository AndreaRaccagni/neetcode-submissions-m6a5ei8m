class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        l = 0
        r = 0

        for i in range(len(s) - 1):
            odd = self.findLongestPalindrome(s, i, i)
            even = self.findLongestPalindrome(s, i, i + 1)

            best = odd if odd['size'] > even['size'] else even
            print(best)

            if max_len < best['size']:
                max_len = best['size']
                l = best['l']
                r = best['r']
        
        res = []
        for i in range(l, r + 1):
            res.append(s[i])

        return ''.join(res)


    def findLongestPalindrome(self, s, i, j):
        l = i
        r = j

        while True:
            if l <= -1 or r >= len(s) or s[l] != s[r]:
                return {
                    'l': l + 1,
                    'r': r - 1,
                    'size': (r - 1) - (l + 1) + 1
                    }

            l -= 1
            r += 1
            

        

                