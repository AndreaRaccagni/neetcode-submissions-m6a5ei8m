class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t: 
                topT, topI = stack.pop()
                result[topI] = i - topI
            
            stack.append((t, i))

        return result
            

