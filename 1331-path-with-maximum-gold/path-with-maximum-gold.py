class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def check(i,j,vismat):
            if(i<0 or j<0 or i==len(grid) or j==len(grid[0])):
                return 0
            if(grid[i][j]==0 or vismat[i][j]==1):
                return 0
            return 1

        def collect(i,j,visited):
            if(check(i,j,visited)==0):
                return 0
            visited[i][j]=1
            ans=max(collect(i+1,j,visited),collect(i-1,j,visited),collect(i,j+1,visited),collect(i,j-1,visited))
            visited[i][j]=0
            return ans+grid[i][j]
        res=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                visited=[[0]*len(grid[0]) for i in range(len(grid))]
                res=max(res,collect(i,j,visited))
        return res