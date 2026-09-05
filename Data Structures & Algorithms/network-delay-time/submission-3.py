class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for src, dest, t in times:
            adj[src].append((dest, t))

        minHeap = [(0, k)]
        seen = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in seen:
                continue

            seen.add(n1)
            if len(seen) == n:
                return t1

            for n2, t2 in adj[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))

        return -1