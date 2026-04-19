class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for n in nums:
            if n in lookup:
                return True
            lookup[n] = True
        return False