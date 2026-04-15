class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) == 0:
            return ""

        def set_contains(needle, haystack):
            for k in needle.keys():
                if k not in haystack or needle[k] > haystack[k]:
                    return False
            return True

        def update_range(c_i, c_j): # j is exclusive
            nonlocal op_tup
            if op_tup is None:
                op_tup = (c_i, c_j)
            if abs(op_tup[0] - op_tup[1]) > abs(c_i - c_j):
                op_tup = (c_i, c_j)
        
        op_tup = None
        lkp1 = {}
        for c in t:
            lkp1[c] = lkp1.get(c, 0) + 1

        lkp2 = {s[0]: 1}
        i = 0
        j = 1

        while True:

            # First evaluate contains
            while set_contains(lkp1, lkp2) and i < j:
                update_range(i,j)
                lkp2[s[i]] -= 1
                if lkp2[s[i]] == 0:
                    del lkp2[s[i]]
                i += 1
            
            if j >= len(s):
                break
            else:
                # now ingest the variable
                lkp2[s[j]] = lkp2.get(s[j], 0) + 1
                j += 1
        
        return s[op_tup[0]:op_tup[1]] if op_tup is not None else ""
            





"""
-> both u&l case

only single freq count matters -> at max 26+26 -> Set 1

substring should contain all from above set at least (can have more than set1)

Appr
- Create a set from t
- In s:
    - Start from i = 0, j=0->n
    - Compare set - if set contains(True) -> Start shrinking i till contains(False)
    - Store substring everytime set contains is True

retrun Subs

"""