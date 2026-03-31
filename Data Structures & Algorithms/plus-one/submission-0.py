class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] * (len(digits) + 1) 
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            carry = 0
            if num > 9:
                carry = 1
                num = 0
            res[i + 1] = num

        if carry:
            res[0] = 1

        return res if res[0] != 0 else res[1:]