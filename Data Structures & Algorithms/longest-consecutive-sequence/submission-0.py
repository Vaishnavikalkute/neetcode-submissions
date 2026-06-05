class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums=set(nums)

        for n in nums:
            cnt,curr=0,n
            while curr in nums:
                cnt+=1
                curr+=1
            res=max(res,cnt)
        
        return res