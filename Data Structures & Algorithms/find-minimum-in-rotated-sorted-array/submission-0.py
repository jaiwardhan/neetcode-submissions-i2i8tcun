class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        
        i = 0
        j = len(nums)-1
        min_item = float('inf')
        while i < j:
            if nums[i] < nums[j]:
                # This range seems sorted already, take first as min and return
                min_item = min(min_item, nums[i])
                break

            mid = i + (j-i)//2
            if nums[mid] < nums[j]:
                # This range seems sorted already, take first as min and go left
                min_item = min(min_item, nums[mid])
                j = mid-1
            else:
                # Partition seems to be on right
                if mid < j:
                    if nums[mid] > nums[mid+1]:
                        # We have found the partition
                        return nums[mid+1]
                # just go right
                i = mid
        
        return min_item



"""
Bf: linear

Opt: sorted around the partition ranges -> think logn
if you can find the partition point, the element next to it could be your min
    -> find middle, (s+e)//2
    -> if middle element is < end -> middle COULD be your minimum
        -> store in min
        and go left(s,mid-1)
    -> if middle is > end -> (Partition is still on the right)
        if mid < e and nums[mid] > nums[mid+1] (This is the partition point)
            store nums[mid+1]
            go right(mid+1,e)
        else go right(mid,e)
        # Watch out for inf loop cases
-> what is array is not partitioned
    nums[s] < nums[e] -> nums[s] -> could be your minimum -> return

[3,4,5,6,1,2]
- [5,6,1,2]
- >1

[3,4,5,6,7,1,2]
- [6,7,1,2]

[1,2,3] -> 1


[6,7,1,2,3,4,5] 
- store 2 go left
- [6,7,1]
- 1

[2,1]
- 1

[5]=> handle sep (cormer)

"""