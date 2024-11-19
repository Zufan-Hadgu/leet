from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        def compare(n1, n2):
            
            if n2 + n1 > n1 + n2:
                return 1
            if n2 + n1 < n1 + n2:
                return -1
            else:
                return 0
        nums = list(map(str, nums))
         
        nums.sort(key=cmp_to_key(compare))
    
        result = ''.join(nums)
        if result[0] == '0':
            return '0'   
        
        return result
