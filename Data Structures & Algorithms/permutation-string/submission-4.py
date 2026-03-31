class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        if window > len(s2):
            return False

        map1 = [0] * 26
        map2 = [0] * 26

        for i in range(window):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1


        count = 0

        for i in range(26):
            count += 1 if map1[i] == map2[i] else 0

        if count == 26:
            return True

        for r in range(window, len(s2)):
            l = r - window
            map2[ord(s2[r]) - ord('a')] += 1
            if map2[ord(s2[r]) - ord('a')] == map1[ord(s2[r]) - ord('a')]:
                count += 1
            else:
                if map2[ord(s2[r]) - ord('a')] - 1 == map1[ord(s2[r]) - ord('a')]:
                    count -= 1

            map2[ord(s2[l]) - ord('a')] -= 1
            if map2[ord(s2[l]) - ord('a')] == map1[ord(s2[l]) - ord('a')]:
                count += 1
            else:
                if map2[ord(s2[l]) - ord('a')] + 1 == map1[ord(s2[l]) - ord('a')]:
                    count -= 1

            if count == 26:
                return True
            
        return False