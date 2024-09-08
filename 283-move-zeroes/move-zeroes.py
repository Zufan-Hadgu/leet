class Solution(object):
    def moveZeroes(self, nums):
        f = 0   
        
        for s in range(len(nums)):
            if nums[s] != 0:   
                if nums[f] == 0:
                     
                    nums[f], nums[s] = nums[s], nums[f]
                f += 1   
        
        return nums
