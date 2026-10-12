class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dest, t in times:
            adj[src].append((dest, t))

        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            
            visited.add(n1)

            if len(visited) == n:
                return t1

            for n2, t2 in adj[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))

        return -1