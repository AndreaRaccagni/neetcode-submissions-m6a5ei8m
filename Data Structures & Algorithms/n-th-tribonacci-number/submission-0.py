class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        
        one = 0
        two = 1
        three = 1

        for i in range(3, n + 1):
            one, two, three = two, three, one + two + three

        return three