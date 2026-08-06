class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxNum = 0
        res = ''

        for i in range(len(num) - 2):
            numStr = num[i:i+3]

            if len(set(numStr)) == 1:
                n = int(numStr)
                maxNum = max(n, maxNum)
                if maxNum == n:
                    res = numStr

        return res