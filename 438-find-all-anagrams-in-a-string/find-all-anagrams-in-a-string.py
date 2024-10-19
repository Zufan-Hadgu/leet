class Solution(object):
    def findAnagrams(self, s, p):
         
        dict_of_p ={}
        for char in p:
            if char in dict_of_p:
                dict_of_p[char] += 1
            else:
                dict_of_p[char] = 1

        dict_of_window = {}
        result = []
        for i in range (len(s)):
            if s[i] in dict_of_window:
                dict_of_window[s[i]] += 1
            else:
                dict_of_window[s[i]] = 1
            
            if i >= len(p):
                if dict_of_window[s[i-len(p)]] == 1:
                    del dict_of_window[s[i-len(p)]]
                else: 
                    dict_of_window[s[i-len(p)]] -= 1
            if dict_of_window == dict_of_p:
                result.append(i-len(p) + 1)
        return result



        
