"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
    # Input: intervals = [(0,40),(5,10),(15,20)]
    # Output: 2

    # (0, 40): heap is empty, so it gets its own room (heap: [40])
    # (5, 10): earliest room frees at 40, and 40 <= 5 is false, so it conflicts
    #          it gets a new room (heap: [10, 40])
    # (15, 20): earliest room frees at 10, and 10 <= 15 is true, so no conflict
    #           pop 10 and push 20 to reuse that room (heap: [20, 40])
    # 2 entries in the heap = 2 rooms

class Solution:
        def minMeetingRooms(self, intervals: List[Interval]) -> int:
            
            intervals.sort(key=lambda i: i.start) # process meetings in order of start time

            minHeap = [] # handles our end values

            # iterate through each interval once
            for interval in intervals:
                # if the room that frees up first (minHeap[0]) is free by the time this meeting starts (interval.start)
                if minHeap and minHeap[0] <= interval.start:
                    heapq.heappop(minHeap) # reuse the room, so we just remove its old meeting end time
                heapq.heappush(minHeap, interval.end) # this meeting now occupies a room until it ends
            
            return len(minHeap) # one entry per room we needed
                