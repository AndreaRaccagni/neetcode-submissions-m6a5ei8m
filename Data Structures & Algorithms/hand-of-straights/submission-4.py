class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        minHeap = []
        for n in count.keys():
            heapq.heappush(minHeap, n)

        while minHeap:
            start = minHeap[0]
            for i in range(groupSize):
                n = start + i
                if n not in count or count[n] == 0:
                    return False

                count[n] -= 1

            while minHeap and count[minHeap[0]] == 0:
                heapq.heappop(minHeap)

        return True