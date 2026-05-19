class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1) - 1

        for r in range(window, len(s2)):
            if self.isAnagram(s1, s2[r - window:r + 1]):
                return True

        return False
        
    
    def isAnagram(self, s1, s2):
        count = [0] * 26

        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False

        return True