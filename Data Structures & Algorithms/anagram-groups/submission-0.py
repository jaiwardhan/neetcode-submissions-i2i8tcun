class Solution:
    ORD_a = ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def ana_codes(s):
            chr_code = [0]*26
            for c in s:
                chr_code[ord(c)-Solution.ORD_a] += 1
            op = ""
            template = "%d-%d_"
            for i in range(26):
                op += (template%(i, chr_code[i]))
            return op
        
        lookup = {}
        for s in strs:
            code = ana_codes(s)
            if code not in lookup:
                lookup[code] = []
            lookup[code].append(s)
        
        return list(lookup.values())

