class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for src, des, w in times:
            adj[src].append((des, w))

        minHeap = []
        heapq.heappush(minHeap, (0, k)) #(w, node)
        res = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in res:
                continue

            res[n1] = w1

            if len(res) == n:
                return w1

            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))

            
        return -1

        