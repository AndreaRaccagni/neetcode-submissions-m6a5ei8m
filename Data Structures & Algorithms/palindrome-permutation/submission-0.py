class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        n = len(s)

        for i in range(n):
            count[s[i]] = count.get(s[i], 0) + 1

        countOdd = 0
        for c in count.values():
            if c % 2 != 0:
                countOdd += 1
                
        return countOdd < 2
            