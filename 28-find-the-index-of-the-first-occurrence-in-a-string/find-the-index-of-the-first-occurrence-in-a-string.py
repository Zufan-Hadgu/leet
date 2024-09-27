class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        s = len(haystack)
        p = len(needle)
        for i in range(s - p +1):
            if haystack[i:p+i] == needle:
                return i
        return -1
         
         

        
        