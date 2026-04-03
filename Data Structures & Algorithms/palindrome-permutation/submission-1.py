class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        odd = 0
        for freq in count.values():
            if freq % 2:
                odd += 1

        return odd < 2
            