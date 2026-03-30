class Solution:
    def get_char_counts(self, s):
        lookup = {}
        for c in s:
            if c not in lookup:
                lookup[c] = 0
            lookup[c] += 1
        
        return lookup

    def isAnagram(self, s: str, t: str) -> bool:
        lookup_s = self.get_char_counts(s)
        lookup_t = self.get_char_counts(t)

        if len(lookup_s.keys()) != len(lookup_t.keys()):
            return False
        for c in lookup_s.keys():
            if c not in lookup_t or lookup_s[c] != lookup_t[c]:
                return False
        
        return True
            