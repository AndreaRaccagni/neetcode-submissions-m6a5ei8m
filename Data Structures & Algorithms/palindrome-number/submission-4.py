class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversedNum = 0
        n = x

        while n:
            reversedNum = reversedNum * 10 + n % 10
            n //= 10

        return x == reversedNum
