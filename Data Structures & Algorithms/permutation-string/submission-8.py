class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ABC_LEN = 26

        counter1 = [0] * ABC_LEN
        counter2 = [0] * ABC_LEN

        for i in range(len(s1)):
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(len(counter1)):
            if counter1[i] == counter2[i]:
                count += 1
        
        window = len(s1)

        for i in range(window, len(s2)):
            if count == ABC_LEN:
                return True

            c2_in = ord(s2[i]) - ord('a')
            counter2[c2_in] += 1
            if counter2[c2_in] - 1 == counter1[c2_in]:
                count -= 1
            elif counter2[c2_in] == counter1[c2_in]:
                count += 1

            c2_out = ord(s2[i - window]) - ord('a')
            counter2[c2_out] -= 1
            if counter2[c2_out] + 1 == counter1[c2_out]:
                count -= 1
            elif counter2[c2_out] == counter1[c2_out]:
                count += 1
            
        return count == ABC_LEN