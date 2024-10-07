class Solution(object):
     
    def targetIndices(self, nums, target):
          
        nums = sorted(nums)
         
        new_list = []
        for i in range(len(nums)):

            if nums[i] ==target:
                new_list.append(i)
        return new_list
                


        