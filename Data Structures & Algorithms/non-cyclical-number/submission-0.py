class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        
        while True:
            slow = self.squaresOfDigits(slow)
            fast = self.squaresOfDigits(self.squaresOfDigits(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False

    def squaresOfDigits(self, n):
        squareOfDigits = 0
        
        while n:
            digit = n % 10
            squareOfDigits += digit * digit
            n //= 10

        return squareOfDigits