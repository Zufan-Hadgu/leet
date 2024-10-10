class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split()
        new_s = []
        for strs in list_s:
            strs[::-1]
            new_s.append(strs[::-1])
        return " ".join(new_s)
        

        