class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited=[[0]*len(grid[0]) for row in grid]

        x=[0,0,-1,1]
        y=[1,-1,0,0]
        def dfs(cx,cy):
            # print(cx,cy)
            if(cx<0 or cy<0 or cx>=len(grid) or cy>=len(grid[0]) or grid[cx][cy]==0 or visited[cx][cy]==1):
                return
            visited[cx][cy]=1
            for i in range(4):
                dfs(cx+x[i],cy+y[i])
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if((i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1) and grid[i][j]==1):
                    # print(i,j)
                    dfs(i,j)
        count=0
        # print(visited)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1 and visited[i][j]!=1):
                    count+=1
        return count