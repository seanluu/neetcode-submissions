"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort all meetings by their start time
        intervals.sort(key=lambda i: i.start)

        # iterate through the sorted list starting from the 2nd meeting
        # by for looping on 1, we skip the 1st meeting...
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1] # interval 1 is the previous meeting
            i2 = intervals[i] # interval 2 is the current meeting

            # 30 > 10
            # 30 > 20, so False
            # basically, if the meeting times overlap, then we return False
            if i1.end > i2.start:
                return False

        # otherwise there is no meeting time overlap so we return True
        return True