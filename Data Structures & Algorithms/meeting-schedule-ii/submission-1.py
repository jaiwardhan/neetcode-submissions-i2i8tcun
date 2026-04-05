"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        rooms = {}
        def find_av_room(interval):
            # If the current room's meeting has ended (not overlapping), we can assign to this room
            for k in rooms.keys():
                if rooms[k].end <= interval.start:
                    return k
            return None
        
        def add_room(interval):
            # Purely assume that we need to create another room with noconflict
            # uuid.uuid4().hex
            room_id = "%d-_-%d"%(interval.start, interval.end)
            rooms[room_id] = interval
        
        def assign_existing(room, interval):
            # Purely assume that the room id is correct
            rooms[room] = interval

        intervals.sort(key=lambda x:x.start)
        for each_i in intervals:
            av = find_av_room(each_i)
            if av is None:
                add_room(each_i)
            else:
                assign_existing(av, each_i)

        return len(rooms.keys())


"""
bf: exponential

opt:
[x,,,,y]1    [x,,,,,,,,y]2    [x,y]3    [x,y]4    
  [x,,,,,,,,,,,y]5  [x,,,,,,,,,,,y]6
       [x,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,y]7

Greedy kindof solution
>sort it
>

{
r1: [x,y]1 -> [x,y]2 -> [x,y]3
r2: [x,y]5 -> [x,y]6 -> [x,y]4
r3: [x,y]7
}

Worst case: n rooms, all overlap, 1,2,3,4...n-1 (n^2)


LSWP: 14,40,000 cycles (1000 meetings, 24h)
n2: 1000000

LSWP: 7500000 cycles (5000 meetings, 24h)
n2:  25000000

"""