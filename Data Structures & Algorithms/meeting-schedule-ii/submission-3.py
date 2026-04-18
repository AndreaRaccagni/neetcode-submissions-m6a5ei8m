"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minHeap = []

        for meeting in intervals:
            if minHeap and minHeap[0] <= meeting.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, meeting.end)

        return len(minHeap)