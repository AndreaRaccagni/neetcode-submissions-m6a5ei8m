class Solution:
    def isHappy(self, n: int) -> bool:
        created = set()
        num = n

        while True:
            if num in created:
                return False
            created.add(num)

            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num = num // 10
            
            if total == 1:
                return True
            num = total