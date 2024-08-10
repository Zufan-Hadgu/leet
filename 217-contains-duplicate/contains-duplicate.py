class Solution(object):
    def containsDuplicate(self, nums):
        set_of_nums = set()  
        
        for num in nums:
            if num in set_of_nums:
                return True   
            set_of_nums.add(num)   
        
        return False   

                
            

        
               
            
         

        
             
         
        