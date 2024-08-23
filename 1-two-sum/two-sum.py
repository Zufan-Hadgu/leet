class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in nums:
                j = nums.index(y)
                if i != j:   
                    return [i, j]

                    

        
        