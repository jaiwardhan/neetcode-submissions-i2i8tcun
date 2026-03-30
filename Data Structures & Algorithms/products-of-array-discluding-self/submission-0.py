class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = [1]*len(nums)
        r_prod = [1]*len(nums)

        i = 1
        prod = 1
        while i < len(nums):
            l_prod[i] = l_prod[i-1]*nums[i-1]
            i += 1
        i = len(nums)-2
        while i >= 0:
            r_prod[i] = r_prod[i+1]*nums[i+1]
            i -= 1
        
        return [l_prod[i]*r_prod[i] for i in range(len(nums))]