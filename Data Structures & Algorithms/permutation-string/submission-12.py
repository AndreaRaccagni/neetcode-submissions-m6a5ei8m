class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        counter = [0] * 26
        shift = ord('a')

        for i in range(n):
            counter[ord(s1[i]) - shift] -= 1
            counter[ord(s2[i]) - shift] += 1

        isPermutation = self.checkCount(counter)
        if isPermutation:
            return True

        for i in range(n, len(s2)):
            right = ord(s2[i]) - shift
            counter[right] += 1

            left = ord(s2[i - n]) - shift
            counter[left] -= 1

            isPermutation = self.checkCount(counter)
            if isPermutation:
                return True

        return False


    def checkCount(self, counter):
        return all(c == 0 for c in counter)
