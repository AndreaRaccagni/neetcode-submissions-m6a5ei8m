class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for x in range(first, first + groupSize):
                if count.get(x, 0) == 0:
                    return False

                count[x] -= 1

                if count[x] == 0:
                    if x != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True