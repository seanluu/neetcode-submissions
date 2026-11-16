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

            minHeap = [] # end time of the current meeting in each room, earliest on top

            # iterate through each interval
            for interval in intervals:
                # if our minHeap is active, and the first element of that min heap is less than or equal to our current starting interval value
                if minHeap and minHeap[0] <= interval.start: 
                    heapq.heappop(minHeap) # pop that top element in our minHeap since we know that it doesn't conflict with our curr starting interval val
                heapq.heappush(minHeap, interval.end) # add the end of the interval to the minHeap

            return len(minHeap)
