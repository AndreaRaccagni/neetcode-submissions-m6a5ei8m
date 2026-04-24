class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                lastT, tIndex = stack.pop()
                res[tIndex] = i - tIndex

            stack.append((t, i))

        return res