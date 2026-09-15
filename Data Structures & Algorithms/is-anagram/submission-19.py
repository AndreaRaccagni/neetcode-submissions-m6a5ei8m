class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        shift = ord('a')

        for i in range(len(s)):
            count[ord(s[i]) - shift] += 1
            count[ord(t[i]) - shift] -= 1

        for c in count:
            if c != 0:
                return False

        return True