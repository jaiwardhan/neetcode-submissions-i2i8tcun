class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = -1
        i = 0
        j = len(heights)-1
        while i < j:
            max_vol = max(max_vol, min(heights[i], heights[j])*(j-i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_vol

    def maxArea_bf(self, heights: List[int]) -> int:
        max_vol = -1
        for i in range(0, len(heights)-1):
            for j in range(i+1, len(heights)):
                max_vol = max(max_vol, min(heights[i], heights[j])*(j-i))
        return max_vol
        

"""
Brute:
Take a wall.
for all walls in i+1:, Compare all min(h, h')*distance with max_vol
=> n^2

If for every index i could know what is the min XX
this problem is about coverage


"""