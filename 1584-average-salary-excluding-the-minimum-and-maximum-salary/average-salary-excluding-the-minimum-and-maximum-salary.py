class Solution(object):
    def average(self, salary):
        salary.sort()
         
        without_min_max = salary[1:-1]
        count = 0
        for i in without_min_max:
            count += i
        
        return float(count) / len(without_min_max)

 

            
        
        