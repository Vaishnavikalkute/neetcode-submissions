class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        cnt=0
        directions=[[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(a,b):
            if a<0 or b<0  or a>=r or b>=c or grid[a][b]=="0":
                return
            grid[a][b]="0"
            for i,j in directions:
                dfs(a+i,b+j)
        
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    dfs(i,j)
                    cnt+=1

        return cnt
        