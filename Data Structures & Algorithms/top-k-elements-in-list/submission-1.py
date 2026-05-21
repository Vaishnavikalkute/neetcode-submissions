class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        obj={}
        for i in nums:
            obj[i]=obj.get(i,0)+1

        obj=sorted(obj.items(),key=lambda x:x[1],reverse=True)

        return [i[0] for i in obj[:k]]

        