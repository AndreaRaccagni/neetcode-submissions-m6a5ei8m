class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and stack[-1][0] < t:
                _, tIndex = stack.pop()
                res[tIndex] = i - tIndex

            stack.append((t, i))

        return res

    [30,38,30,36,35,40,28]
    i = 5
    t = 40
    stack = [(40, 5), (28, 6)]
    res = [1, 4, 1, 2, 1, 0, 0]