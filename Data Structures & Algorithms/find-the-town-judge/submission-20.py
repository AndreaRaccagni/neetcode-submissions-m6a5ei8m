class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = {}
        incoming = {}

        for o, i in trust:
            outgoing[o] = 1
            incoming[i] = incoming.get(i, 0) + 1

        judge = -1

        if len(outgoing) == n - 1 and list(incoming.values())[0] == n - 1:
            judge = list(incoming.keys())[0]

        return judge