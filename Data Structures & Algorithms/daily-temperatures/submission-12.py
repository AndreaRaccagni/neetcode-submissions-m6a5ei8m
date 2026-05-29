class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
 
            while stack and curr_temp > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index
            
            stack.append((curr_temp, i))

        return res