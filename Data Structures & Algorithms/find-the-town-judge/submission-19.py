class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        sources = {}
        receivers = {}

        for source, receiver in trust:
            sources[source] = sources.get(source, 0) + 1
            receivers[receiver] = receivers.get(receiver, 0) + 1

        for i in range(1, n + 1):
            if sources.get(i, 0) == 0 and receivers.get(i, 0) == n - 1:
                return i

        return -1