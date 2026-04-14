class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        p = 0

        while p < len(asteroids):
            if not stack or stack[-1] * asteroids[p] > 0 or (stack[-1] < 0 and asteroids[p] > 0):
                stack.append(asteroids[p])
                p += 1
            else:
                if abs(stack[-1]) == abs(asteroids[p]):
                    stack.pop()
                    p += 1
                elif abs(stack[-1]) > abs(asteroids[p]):
                    p += 1
                else:
                    stack.pop()

        return stack
