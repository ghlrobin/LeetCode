class Solution:
    def isValid(self, s: str) -> bool:
    
        # if length of s is odd then s is invalid    
        if len(s) % 2 == 1:
            return False
        
        brackets = {'(': ')',
            '[': ']',
            '{': '}'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                if stack and char == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else: return True
                        
                    
                

            
            
                
                

                
        