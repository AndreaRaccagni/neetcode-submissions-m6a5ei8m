class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        lenAbc = 26
        window = len(s1)
        s1Map = [0] * lenAbc
        s2Map = [0] * lenAbc
        matches = 0

        for i in range(window):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        for i in range(lenAbc):
            if s1Map[i] == s2Map[i]:
                matches += 1

        for i in range(window, len(s2)):
            if matches == lenAbc:
                return True

            # remove left char
            left = ord(s2[i - window]) - ord('a')
            s2Map[left] -= 1
            if s2Map[left] == s1Map[left]:
                matches += 1
            elif s2Map[left] + 1 == s1Map[left]:
                matches -= 1

            # add right char
            right = ord(s2[i]) - ord('a')
            s2Map[right] += 1
            if s2Map[right] == s1Map[right]:
                matches += 1
            elif s2Map[right] - 1 == s1Map[right]:
                matches -= 1

        return matches == lenAbc