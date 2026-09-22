class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)

        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: x[0])
        stack = [cars[0]]

        for i in range(1, n):
            p2, s2 = cars[i]
            hrs_2 = (target - p2) / s2
            
            while stack and (target - stack[-1][0]) / stack[-1][1] <= hrs_2:
                stack.pop()

            stack.append(cars[i])

        return len(stack)

