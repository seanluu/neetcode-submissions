"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort meetings by start time, so any overlap has to be between neighbors
        intervals.sort(key=lambda i: i.start)

        # start at 1 so every meeting has a previous one to compare with
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # previous meeting
            i2 = intervals[i]  # current meeting

            # overlap if the previous meeting ends after the current one starts
            # (> not >=, since ending at 10 and starting at 10 is fine)
            # e.g. [0,30] and [5,10]: 30 > 5, so they overlap
            if i1.end > i2.start:
                return False

        # no neighbors overlap, so you can attend every meeting
        return True