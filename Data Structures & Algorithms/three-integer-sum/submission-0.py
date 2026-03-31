class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []

        i = 0
        while i < len(nums)-2:
            j = i + 1
            k = len(nums)-1
            target = -(nums[i])
            
            while j < k:
                c_sum = nums[j] + nums[k]
                # Overshooting the target:
                if c_sum > target:
                    k -= 1
                # Under achieve the target
                elif c_sum < target:
                    j += 1
                else:
                    # Valid trip found
                    op.append([nums[i], nums[j], nums[k]])
                    j_new = j
                    while j_new < k and nums[j] == nums[j_new]:
                        j_new += 1
                    j = j_new
                    k_new = k
                    while k_new > j and nums[k] == nums[k_new]:
                        k_new -= 1
                    k = k_new
            i_new = i
            while i_new < len(nums)-2 and nums[i] == nums[i_new]:
                i_new += 1
            i = i_new
        return op