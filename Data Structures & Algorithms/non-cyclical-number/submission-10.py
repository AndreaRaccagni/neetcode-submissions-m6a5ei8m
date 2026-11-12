class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while True:
            if curr in seen:
                return False
            seen.add(curr)

            happy = 0
            while curr:
                digit = curr % 10
                happy += digit * digit
                curr = math.floor(curr / 10)
            
            if happy == 1:
                return True

            curr = happy
