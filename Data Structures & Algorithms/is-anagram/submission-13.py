class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        abc = [0] * 26

        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            abc[s_index] += 1
            abc[t_index] -= 1

        for count in abc:
            if count != 0:
                return False

        return True