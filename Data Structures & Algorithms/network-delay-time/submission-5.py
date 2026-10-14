class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)

        for src, dest, t in times:
            network[src].append((dest, t)) #in map destination, time

        minHeap = [(0, k)] #in minHeap time, node
        time = 0
        visited = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue

            visited.add(n1)

            if len(visited) == n:
                return t1

            for n2, t2 in network[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))

        return -1