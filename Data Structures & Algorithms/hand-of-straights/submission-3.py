class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        minHeap = list(set(hand))
        heapq.heapify(minHeap)

        while minHeap:
            if count[minHeap[0]] == 0:
                heapq.heappop(minHeap)
                continue
            
            start = minHeap[0]
     
            for i in range(groupSize):
                if start + i not in count or count[start + i] == 0:
                    return False

                count[start + i] -= 1

        return True

