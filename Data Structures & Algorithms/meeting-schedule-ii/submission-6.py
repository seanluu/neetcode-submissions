"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

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
