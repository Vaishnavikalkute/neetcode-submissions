class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=[]

        r,c=len(grid),len(grid[0])

        dirc=[[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    queue.append((i,j))

        inf=2147483647

        while queue:
            a,b=queue.pop(0)

            for nr,nc in dirc:
                na,nb=nr+a,nc+b
                if na<0 or nb<0 or na>=r or nb>=c or grid[na][nb]!=inf:
                    continue

                grid[na][nb]=grid[a][b]+1

                queue.append((na,nb))