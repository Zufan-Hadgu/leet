class Solution(object):
    
    
    def longestPalindrome(self, s):
        def checking(l,r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return s[l + 1: r]
        longest = ""
        for i in range(len(s)):
            odd = checking(i,i)
            even = checking(i, i+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest


        


         
        