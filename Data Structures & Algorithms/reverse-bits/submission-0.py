class Solution:
    def reverseBits(self, n: int) -> int:
        bin_data = []
        op = 0
        count = 0
        while n > 0:
            b = n%2
            n //= 2
            op += 2**(31-count) if b > 0 else 0
            count += 1
        return op

"""
store existing binary data in bin_data
start from bin_data -> 0 index => 2^(32-1-0) + .. 2^(32-1-k)+..

or we can do it on the fly

"""