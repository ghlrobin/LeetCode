class Solution:
    def isValid(self, s: str) -> bool:
    
        # if length of s is odd then s is invalid    
        if len(s) % 2 == 1:
            return False
        
        # replace {}, (), [] with ''
        k = ['[]', '{}', '()']
        n = len(s) // 2
        for _ in range(n):
            for x in k:
                s = s.replace(x, '')
                
        if s:
            return False
        else:
            return True
                

            
            
                
                

                
        