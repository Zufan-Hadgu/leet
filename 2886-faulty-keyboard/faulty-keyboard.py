class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_str = ""
        for char in s:
            if char == "i":
                new_str = new_str[::-1]
            else:
                new_str += char   
        return new_str
            

        