class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = {}
        incoming = {}

        for o, i in trust:
            outgoing[o] = outgoing.get(o, 0) + 1
            incoming[i] = incoming.get(i, 0) + 1

        for i in range(1, n + 1):
            if i not in outgoing and incoming.get(i) == n - 1:
                return i

        return -1