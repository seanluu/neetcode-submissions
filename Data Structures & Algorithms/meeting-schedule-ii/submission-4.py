"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

    # Input: intervals = [(0,40),(5,10),(15,20)]
    # Output: 2

    # r1: (0, 40)
    # r2: (5, 10), (15, 20)

    # we separate them into two separate rooms since if we were to include (0, 40), 
    # then it overlaps while (5, 10) and (15, 20) are still ongoing.
    # (5, 10) and (15, 20) can use the same room since (5, 10) ends before (15, 20)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted(i.start for i in intervals) # all start times, sorted
        end = sorted(i.end for i in intervals) # all end times, sorted

        res, count = 0, 0 # res is the answer (most meetings at once), count is meetings happening right now

        s, e = 0, 0 # s is our position in start, e is our position in end

        while (s < len(intervals)):
            # if the next meeting starts before the earliest unfinished one ends
            if start[s] < end[e]:
                count += 1 # one more meeting happening at once
                s += 1 # move to the next start time
            else:
                count -= 1 # a meeting ended, so one fewer happening
                e += 1 # move to the next end time
            res = max(res, count) # keep the most meetings we've seen at once, that's how many rooms we need

        return res