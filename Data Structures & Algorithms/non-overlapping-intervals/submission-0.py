class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        prev = 0
        remove_count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                remove_count += 1
                prev = prev if intervals[prev][1] < intervals[i][1] else i
            else:
                prev = i
        
        return remove_count


"""

define overlapping(Strict/boundary)?

                           [x,y]8
  [x,y]1    [x,y]2     -[x,,,,,,,,,,,,y]3-    [x,y]4
    --[x,,,,,,,,,,,,,,,,,,,,,,,,y]5--


  [x,y]1            [x,y]2           [x,y]3    [x,y]4
         [x,,,,y]5
> Sorted by 1st

[x,y]1 OV: [x,,,,,,,,,,,,,,,,y]5

-> Sort the list
-> Start by comparing paris from the start (previous = 0)
-> For current 1:end
    -> If current overlaps with previous
        We need to remove one of them - which one?
            [x ] - If we removed x1y1-> (take max of x1y1,x5y5), then i end up removing x2y2 x3y3 
            [_/] - If we removed x5y5-> (take min of x1y1,x5y5), then i end up removing nothing else
    -> Else
        Move prev to current

"""