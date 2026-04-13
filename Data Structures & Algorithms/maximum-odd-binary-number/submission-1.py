class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)

        res = ''

        while '1' in count and count['1'] > 1:
            res += '1'
            count['1'] -= 1

        if '0' in count:
            res += '0' * count['0']

        return res + '1' if '1' in count else res