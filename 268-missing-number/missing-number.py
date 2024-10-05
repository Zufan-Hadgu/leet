class Solution(object):
    def sorting(self, numss):
            if len(numss) <= 1:
                return numss
            m = len(numss) // 2
            l = numss[:m]
            r = numss[m:]
            self.sorting(l)
            self.sorting(r)

            i = 0
            j = 0 
            k = 0

             
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    numss[k] = l[i]
                    i += 1
                else:
                    numss[k] = r[j]
                    j += 1
                k += 1

             
            while i < len(l):
                numss[k] = l[i]
                i += 1
                k += 1

             
            while j < len(r):
                numss[k] = r[j]
                j += 1
                k += 1

            return numss
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = self.sorting(nums)
        n = len(nums)

        
        for i in range(n + 1):   
            if i not in nums:
                return i
