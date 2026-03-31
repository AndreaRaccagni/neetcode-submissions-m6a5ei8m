class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = [0] * 26
        map2 = [0] * 26

        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(len(map1)):
            if map1[i] == map2[i]:
                count += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if count == 26:
                return True

            index = ord(s2[r]) - ord('a')
            map2[index] += 1
            if map1[index] == map2[index]:
                count += 1
            elif map2[index] - 1 == map1[index]:
                count -= 1

            index = ord(s2[l]) - ord('a')
            map2[index] -= 1
            if map1[index] == map2[index]:
                count += 1
            elif map2[index] + 1 == map1[index]:
                count -= 1
            
            l += 1

        return count == 26

        
        