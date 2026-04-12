class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        strNum = str(x)

        l = 0
        r = len(strNum) - 1

        while l < r:
            if strNum[l] != strNum[r]:
                return False

            l += 1
            r -= 1

        return True