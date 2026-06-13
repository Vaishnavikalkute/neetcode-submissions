class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stc=[]


        for i in tokens:
            if i == "+":
                stc.append(stc.pop()+stc.pop())
            elif i == "-":
                a=stc.pop() 
                b=stc.pop() 
                stc.append(b-a)
            elif i == "*":
                stc.append(stc.pop()*stc.pop())
            elif i == "/":
                a=stc.pop() 
                b=stc.pop() 
                stc.append(int(b/a))
            else:
                stc.append(int(i))
        return stc.pop()