class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        fresh=0
        time=0
        dirc=[[1,0],[0,1],[-1,0],[0,-1]]
        r,c=len(grid),len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))

        while fresh>0 and q:
            # all the rotton will start rotten other nb in every min together

            for i in range(len(q)):
                nr,nc=q.pop(0)

                for dr,dc in dirc:
                    a,b=dr+nr,dc+nc

                    if a<0 or b<0 or a>=r or b>=c or grid[a][b]==0 or grid[a][b]==2:
                        continue
                    grid[a][b]=2
                    fresh-=1
                    q.append((a,b))
                
            time+=1

        return time if fresh==0 else -1

        
        