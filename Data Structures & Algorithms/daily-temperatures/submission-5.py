class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                [last_t, last_i] = stack.pop()
                res[last_i] = i - last_i

            stack.append((t, i))

        return res 
