class Solution(object):
    def longestCommonPrefix(self, strs):
       
        lists = []
        for string in strs:
            lists.append(list(string))
        
       
        common_prefix = []
        
        min_length = min(len(lst) for lst in lists)
        
        for i in range(min_length):
             current_char = lists[0][i]
            
             if all(lst[i] == current_char for lst in lists):
                common_prefix.append(current_char)
             else:
                break
        
        return ''.join(common_prefix)
 

        
       
        