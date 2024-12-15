class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0 
        b = int(math.sqrt(c))
        
        while a <= b:
            number  = a * a + b * b 
            if number == c:
                return True
            elif number < c:
                a += 1
            else:
                b -= 1
        return False
        