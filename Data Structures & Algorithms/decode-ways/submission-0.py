class Solution:
    def numDecodings(self, s: str) -> int:
        
        def is_valid(s):
            if len(s) == 0 or s[0] == "0":
                return False
            num = int(s)
            return num >= 1 and num <= 26
        
        memo = {}
        def decode_helper(index):
            if index >= len(s):
                return 1
            if index in memo:
                return memo[index]
            current_w = 0
            next_w = 0
            if index+1 <= len(s) and is_valid(s[index:index+1]):
                current_w = decode_helper(index+1)
            if index+2 <= len(s) and is_valid(s[index:index+2]):
                next_w = decode_helper(index+2)
            
            memo[index] = current_w + next_w
            return current_w + next_w
        
        return decode_helper(0)
                

"""
1012 << 1
1 + s012 <<INV 0 

10 + s12 << 2
    - 1 + s2
            2 + "" <<1
    - 12 + "" << 1


01
<< INV+0

1113 << 5
1 + s113 << 3
    1 + s13 << 2
        1 + s3
            3 + "" << 1
        13 + "" << 1
    11 + s3 << 1

11 + s13 << 2
    1 + s3
        3 + "" << 1
    13 + "" << 1

"""