class Solution(object):
    def majorityElement(self, nums):
        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        
        result = []
        for num in elements:
            if elements[num] > len(nums) / 3:
                result.append(num)
        
        return result
