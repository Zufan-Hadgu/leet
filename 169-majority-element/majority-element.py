class Solution(object):
    def majorityElement(self, nums):
        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        for num in elements:
            if elements[num] > len(nums)/2:
                return num

        
        