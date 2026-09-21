class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26
        shift = ord('a')

        for i in range(n):
            s1_map[ord(s1[i]) - shift] += 1
            s2_map[ord(s2[i]) - shift] += 1

        counter = 0
        for i in range(len(s1_map)):
            counter += 1 if s1_map[i] == s2_map[i] else 0
        
        if counter == 26:
            return True

        for r in range(n, len(s2)):
            l = r - n
            r_index = ord(s2[r]) - shift
            s2_map[r_index] += 1
            if s2_map[r_index] == s1_map[r_index]:
                counter += 1
            elif s2_map[r_index] - 1 == s1_map[r_index]:
                counter -= 1
            
            l_index = ord(s2[l]) - shift
            s2_map[l_index] -= 1
            if s2_map[l_index] == s1_map[l_index]:
                counter += 1
            elif s2_map[l_index] + 1 == s1_map[l_index]:
                counter -= 1

            if counter == 26:
                return True

        return False

