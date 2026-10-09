class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [] #count
        q = deque() #(count, nextTime)
        time = 0

        for cnt in count.values():
            heapq.heappush(maxHeap, -cnt)

        while q or maxHeap:
            time += 1
            
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append((count, time + n))
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time