class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        l,r=0,1
        n=len(s)
        cnt=0
        for r in range(n):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            r+=1
            cnt=max(cnt,r-l)
        return cnt

        