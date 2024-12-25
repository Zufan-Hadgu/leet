class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        
        for char in s:
            if char.isalpha():
                stack.append(char)
            elif stack:
                stack.pop()
        
        stack2 = []
        
        for char in t:
            if char.isalpha():
                stack2.append(char)   
            elif stack2:
                stack2.pop()
         
         
        return "".join(stack2) == "".join(stack)
