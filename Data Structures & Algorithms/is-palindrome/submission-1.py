class Solution:
    ORD_a = ord('a')
    ORD_z = ord('z')
    ORD_0 = ord('0')
    ORD_9 = ord('9')

    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        def travel_ltor_till_not_alphanum(i):
            while i < len(s) and \
                (ord(s[i]) > Solution.ORD_z or ord(s[i]) < Solution.ORD_a) and \
                (ord(s[i]) > Solution.ORD_9 or ord(s[i]) < Solution.ORD_0):
                i += 1
            return i
        
        def travel_rtol_till_not_alphanum(j):
            while j >= 0 and \
                (ord(s[j]) > Solution.ORD_z or ord(s[j]) < Solution.ORD_a) and \
                (ord(s[j]) > Solution.ORD_9 or ord(s[j]) < Solution.ORD_0):
                j -= 1
            return j
        
        s = s.lower()
        i = travel_ltor_till_not_alphanum(0)
        j = travel_rtol_till_not_alphanum(len(s)-1)
        
        # main loop
        while i < j:
            if s[i] != s[j]:
                return False
            i = travel_ltor_till_not_alphanum(i+1)
            j = travel_rtol_till_not_alphanum(j-1)
        
        return True