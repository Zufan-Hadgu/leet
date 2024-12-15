class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        array_of_nums = []
        if num % 3 == 0:
            x = num // 3
            array_of_nums.append(x-1)
            array_of_nums.append(x)
            array_of_nums.append(x+1)
        return array_of_nums

         
   

   