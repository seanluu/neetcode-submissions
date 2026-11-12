"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start) # sort meetings by their start time, any overlap has to be neighbors

        for i in range(1, len(intervals)): # start after 1 since we'll need to compare to original meeting room for conflict
            i1 = intervals[i - 1] # room before i2
            i2 = intervals[i] # regular room

            if i1.end > i2.start: # rooms overlap if the prev meeting ends after the curr one starts
                return False

        return True
