class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_lcs = -1
        
        num = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            # If we can expand the range, continue expanding
            if nums[i] > num + 1:
                # Start of a new range, update previous max lcs
                max_lcs = max(max_lcs, cnt)
                num = nums[i]
                cnt = 1
            elif nums[i] == num + 1:
                # We can continue expansion
                num = nums[i]
                cnt += 1

        max_lcs = max(max_lcs, cnt)
        return max_lcs

"""
- sort- [2,3,4,4,5,10,20]

- [0,3,2,5,4,6,1,1]
->[0,1,1,2,3,4,5,6]

[-10,-9,-8,1,1,2,3,4,5,6]

- sort the list
- start from first index, count 1
- in range(i+1:)
    - if number > base +1
        update max lcs
        update base num
    - else
        continue expanding the range 
        base num = new num

update max lcs again with data
"""