class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stck=[]
        for p,s in sorted(pair)[::-1]: #reveerse traverse
            stck.append((target-p)/s)
            if len(stck)>1 and stck[-1]<=stck[-2]:
                stck.pop()
        return len(stck)