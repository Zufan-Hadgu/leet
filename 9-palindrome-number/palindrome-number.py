class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        old_int = x
        palindrom = []
        while x > 0:
            n = x%10
            palindrom.append(n)
            x = x//10
        reversed_number = int("".join(map(str, palindrom)))
        return reversed_number == old_int
        
        