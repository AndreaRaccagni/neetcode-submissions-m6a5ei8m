class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        sources = {}
        receivers = {}

        for source, receiver in trust:
            receivers[source] = receivers.get(source, 0) + 1
            sources[receiver] = sources.get(receiver, 0) + 1

        for i in range(1, n + 1):
            if receivers.get(i, 0) == 0 and sources.get(i, 0) == n - 1:
                return i

        return -1