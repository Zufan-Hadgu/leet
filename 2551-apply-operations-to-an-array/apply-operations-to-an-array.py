class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i < len(nums) -1:
                if nums[i] ==nums[i +1]:
                    nums[i] = nums[i] * 2
                    nums[i + 1] = 0
        f = 0   
        
        for s in range(len(nums)):
            if nums[s] != 0:   
                if nums[f] == 0:
                     
                    nums[f], nums[s] = nums[s], nums[f]
                f += 1   
        
        return nums

   