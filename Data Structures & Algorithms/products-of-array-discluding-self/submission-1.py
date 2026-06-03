class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lft=[1]*n

        rgt=[1]*n
        res=[1]*n

        for i in range (1,n):
            # skip the 1st value as there is nothing at lft of it
            lft[i]=lft[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            # skip the n-1 value as there is nothing at rgt of it
            rgt[i]=rgt[i+1]*nums[i+1]

        for i in range(n):
            res[i]=lft[i]*rgt[i]

        return res