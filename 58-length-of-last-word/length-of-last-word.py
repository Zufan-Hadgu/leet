class Solution(object):
   def lengthOfLastWord(self, s):
     words = s.strip().split()
     if words:
        last_word = words[-1]
        return len(last_word)
     else:
        return 0

        
        