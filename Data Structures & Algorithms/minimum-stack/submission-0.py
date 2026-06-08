class MinStack:

    def __init__(self):
        self.stc=[]
        

    def push(self, val: int) -> None:
        return self.stc.append(val)
        
        

    def pop(self) -> None:
        return self.stc.pop()
        

    def top(self) -> int:
        return self.stc[-1]
        

    def getMin(self) -> int:
        return min(self.stc)
