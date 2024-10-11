class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        first_sum = sum(nums[:k])
        max_sum = first_sum
        for i in range(k,len(nums)):
            first_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum,first_sum)
        return  float(max_sum)/k
             




        