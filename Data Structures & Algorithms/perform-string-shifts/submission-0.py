class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        p = 0

        for direction, amount in shift:
            if direction == 0:
                p = (p + amount) % len(s)
            else:
                p -= amount
                if p < 0:
                    p = len(s) + p

        return s[p:] + s[:p]