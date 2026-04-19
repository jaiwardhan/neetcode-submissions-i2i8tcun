class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rob_helper(st):
            if st >= len(nums):
                return 0
            if st in memo:
                return memo[st]
            s1 = nums[st] + rob_helper(st+2)
            s2 = rob_helper(st+1)
            memo[st] = max(s1,s2)
            return memo[st]
        
        return rob_helper(0)


"""
brute:
at every house from 0, you can choose to rob or not rob
-> S1 = if robbing at i, evaluate nums[i] + (i+2..)
-> S2 = evaluate(i+1...)
-> return max s1,s2


Overlapping subproblems from the subsets -> memoize
"""