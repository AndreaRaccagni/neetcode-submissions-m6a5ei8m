class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))

        return res