class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        counter = [0] * 26
        shift = ord('a')
        for i in range(n):
            counter[ord(s1[i]) - shift] += 1
            counter[ord(s2[i]) - shift] -= 1
        
        if self.isPermutation(counter):
            return True

        for i in range(n, len(s2)):
            counter[ord(s2[i]) - shift] -= 1
            counter[ord(s2[i - n]) - shift] += 1

            if self.isPermutation(counter):
                return True

        return False

    def isPermutation(self, arr: List[int]) -> bool:
        for n in arr:
            if n != 0:
                return False

        return True