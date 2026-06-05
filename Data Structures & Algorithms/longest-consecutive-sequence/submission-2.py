class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res=0
        # nums=set(nums)

        # for n in nums:
        #     cnt,curr=0,n
        #     while curr in nums:
        #         cnt+=1
        #         curr+=1
        #     res=max(res,cnt)
        
        # return res


        mp=defaultdict(int)
        cnt=0

        for n in nums:
            if not mp[n]:
                mp[n]=mp[n-1]+mp[n+1]+1
                mp[n+mp[n+1]]=mp[n]
                mp[n-mp[n-1]]=mp[n]
                
                cnt=max(cnt,mp[n])
            # print(mp)
            # print(cnt)

        return cnt