class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            
            obj[tuple(count)].append(i)
        print(obj.values())
        return list(obj.values())