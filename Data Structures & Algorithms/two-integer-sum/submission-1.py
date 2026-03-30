class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in lookup:
                return [lookup[t], i]
            lookup[nums[i]] = i
        return [0,0]

"""
-> Positional matters (no sort)
Base soln: n^2
a + b = sum
-> sum - a = b
if b exists then -> a,b coods
else
{
    a: cood
}

"""