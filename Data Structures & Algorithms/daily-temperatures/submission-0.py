class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t: 
                popped = stack.pop()
                result[popped[1]] = i - popped[1]
            
            stack.append((t, i))

        return result
            

