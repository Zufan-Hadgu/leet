class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict_t = {}
        for char in t:
             dict_t[char] = dict_t.get(char,0) + 1
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        
        return dict_s == dict_t


         
        