class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lookup = {}
        lower_b, upper_b = 0,0
        lookup[s[0]] = 0
        mx_len = upper_b - lower_b + 1
        for i in range(1, len(s)):
            if s[i] in lookup:
                # lower_b = lookup[s[i]]+1
                lower_b = max(lower_b, lookup[s[i]]+1)
            lookup[s[i]] = i
            upper_b = i
            mx_len = max(mx_len, upper_b - lower_b + 1)
        
        return mx_len

"""
abcbde

-> Take a left bound and right bound index (0,0)
-> keep a lookup where:
    - if currchar is not in lookup: => add new
    - if currchar is in lookup:
        shift lower bound to the right of the previous occurrence of currchar
    - add/update character's last occurrence and update right bound
    - max len will be (r-l+1)

"""