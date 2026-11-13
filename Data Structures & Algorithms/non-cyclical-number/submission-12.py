class Solution:
    def isHappy(self, n: int) -> bool:
        created = set()
        curr = n

        while True:
            if curr in created:
                return False
            created.add(curr)
            happy = 0

            while curr:
                digit = curr % 10
                happy += digit * digit
                curr = curr // 10
            
            if happy == 1:
                return True

            curr = happy