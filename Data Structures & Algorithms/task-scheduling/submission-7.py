class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = []
        q = deque()
        time = 0

        for count in counter.values():
            heapq.heappush(maxHeap, -count)

        while q or maxHeap:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time