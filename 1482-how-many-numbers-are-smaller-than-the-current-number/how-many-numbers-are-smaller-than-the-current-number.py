class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        new_list= []
        for num in nums:
            number = 0
            for i in range(0,len(nums)):
                if num > nums[i]:
                    number += 1
                elif num <= nums[i]:
                    continue
            new_list.append(number)
        return new_list



         