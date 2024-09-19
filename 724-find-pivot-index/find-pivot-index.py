class Solution(object):
    def pivotIndex(self, nums):
        ls= 0
        ts  = sum(nums) 
        for i in range(len(nums)):
            rs = ts - ls -nums[i]
            if ls == rs:
                 return i 
            ls += nums[i]
        return -1
    
      

            
           