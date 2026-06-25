class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        
        for i in range(len(s)):
            total += self.countPalindromes(s, i, i)
            total += self.countPalindromes(s, i, i + 1)

        return total

    
    def countPalindromes(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count