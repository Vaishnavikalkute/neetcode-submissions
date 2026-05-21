class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirc=[[1,0],[0,1],[-1,0],[0,-1]]
        max_i=0
        cnt=0
        r,c=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 0 
            grid[i][j]=0
            cnt=1
            for ir,jc in dirc:
                cnt+=dfs(i+ir,j+jc)
            return cnt
        
        for a in range(r):
            for b in range(c):
                if grid[a][b]==1:
                    cnt=dfs(a,b)
                    print(cnt)
                    max_i=max(cnt,max_i)
        return max_i