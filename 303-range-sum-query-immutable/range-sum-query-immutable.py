class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        
        

    def sumRange(self, left, right):
        prefix_sum = 0
        for i in range(left, right+1 ):
            prefix_sum += self.nums[i]
        return prefix_sum

         
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)