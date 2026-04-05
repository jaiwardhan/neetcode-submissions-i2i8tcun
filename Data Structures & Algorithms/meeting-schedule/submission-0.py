"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x:x.start)
        
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[prev].end:
                return False
            prev = i
        
        return True




"""
Overlaps: strict or end excluded? - end overlap does not count

- sort the meetings to have a better picture
- start from previous: 0
- for i in range(1,end)
    - if current meeting starts after previous: OK
    - early exit false
- You can attend all: return true


if there are no meetings? :: no conflict, true
"""