class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = 0
        r = 1
        dif = 0
        while r < len(nums):
            value =  nums[r] - nums[l] 
            if value > dif:
                dif = value
            l += 1
            r += 1
        return dif


        