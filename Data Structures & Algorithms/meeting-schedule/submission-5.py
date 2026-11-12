"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1] # lags behind i2 by 1 index
            i2 = intervals[i] # original

            # if interval 1's end overlaps with the start of interval 2's start,
            # then we return False since we do have a conflict
            if i1.end > i2.start:
                return False

        return True