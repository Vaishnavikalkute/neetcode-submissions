class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lft=[1]*n

        rgt=[1]*n
        res=[1]*n

        for i in range (1,n):
            lft[i]=lft[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rgt[i]=rgt[i+1]*nums[i+1]

        for i in range(n):
            res[i]=lft[i]*rgt[i]

        return res