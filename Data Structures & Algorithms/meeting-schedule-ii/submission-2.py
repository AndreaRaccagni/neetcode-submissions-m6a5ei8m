"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for meeting in intervals:
            starts.append(meeting.start)
            ends.append(meeting.end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0
        currRooms = 0
        maxRooms = currRooms

        while s < len(starts):
            if starts[s] < ends[e]:
                currRooms += 1
                s += 1
                maxRooms = max(currRooms, maxRooms)
            else:
                currRooms -= 1
                e += 1

        return maxRooms
        