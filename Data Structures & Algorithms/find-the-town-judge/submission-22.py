class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = {}
        incoming = {}

        for o, i in trust:
            outgoing[o] = outgoing.get(o, 0) + 1
            incoming[i] = incoming.get(i, 0) + 1

        for candidate, votes in incoming.items():
            if candidate not in outgoing and votes == n - 1:
                return candidate

        return -1