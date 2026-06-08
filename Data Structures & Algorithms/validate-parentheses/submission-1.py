class Solution:
    def isValid(self, s: str) -> bool:
        stc=[]
        for i in s:
            if i in ["(","[","{"]:
                stc.append(i)
            else:
                if stc:
                    last=stc.pop()
                else:
                    return False
                if last=="{" and i=="}":
                    continue        
                if last=="(" and i==")":
                    continue        
                if last=="[" and i=="]":
                    continue 
                return False

        return True if len(stc)==0 else False       
