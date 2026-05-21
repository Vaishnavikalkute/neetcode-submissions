class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj={}
        if len(s)!=len(t):
            return False
        for i in s:
            obj[i]=obj.get(i,0)+1
        
        for j in t:
            if j in obj:
                obj[j]-=1
            else:
                return False

            if obj[j]<0:
                return False
            
        return True