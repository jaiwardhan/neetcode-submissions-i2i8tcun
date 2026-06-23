class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lookup = {}
        start = 0
        end = 0
        max_l = 0

        while end < len(s):
            # Contraction
            while s[end] in lookup:
                del lookup[s[start]]
                start += 1
            
            # Expand
            lookup[s[end]] = True
            # Compute
            max_l = max(max_l, end-start+1)
            end += 1
        return max_l