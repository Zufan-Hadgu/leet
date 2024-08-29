class Solution(object):
    def romanToInt(self, s):
        Roman_numbers = {
              'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000
            } 
        total = 0
        n = len(s)
        
        for i in range(n):
            
            value = Roman_numbers[s[i]]
            
            
            if i < n - 1 and value < Roman_numbers[s[i + 1]]:
                total -= value
            else:
                total += value
        
        return total

        

        
        