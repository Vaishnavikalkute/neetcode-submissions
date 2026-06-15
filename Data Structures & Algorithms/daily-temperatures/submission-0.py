class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stc=[]
        for i,v in enumerate(temperatures):
            while stc and stc[-1][1]<v:
                stci,stcv=stc.pop()
                res[stci]=i-stci
            stc.append((i,v))

        return res

        