class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(0,len(grid)):
            if(grid[i][0]==0):
                for j in range(0,len(grid[0])):
                    grid[i][j]=(grid[i][j]+1)%2
        for i in range(0,len(grid[0])):
            c=0
            for j in range(0,len(grid)):
                if(grid[j][i]==1):
                    c+=1
            if(c<(n//2+n%2)):
                for j in range(0,len(grid)):
                    grid[j][i]=(grid[j][i]+1)%2
        
        res=0
        for row in grid:
            res+=int("".join(map(str,row)),2)
        return res