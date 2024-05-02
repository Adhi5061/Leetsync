class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        


        row=len(obstacleGrid)
        col=len(obstacleGrid[0])

        memo={}
        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==row-1 and j==col-1 and obstacleGrid[i][j]!=1):
                memo[(i,j)]=1
                return 1
            if(i>=row or j>=col):
                memo[(i,j)]=0
                return 0
            if(obstacleGrid[i][j]==1):
                memo[(i,j)]=0
                return 0
            ans=dp(i+1,j)+dp(i,j+1)
            memo[(i,j)]=ans
            return ans
        return dp(0,0)


        # d={}
        # m=len(obstacleGrid)-1
        # n=len(obstacleGrid[0])-1
        # print(m,n)
        # def path(x,y):
        #     if((x,y) in d):
        #         return d[(x,y)]
        #     if(x>m or y>n):
        #         return 0
        #     if(obstacleGrid[x][y]==1):
        #         d[(x,y)]=0
        #         return 0
        #     if(x==m and y==n):
        #         d[(x,y)]=1
        #         return 1
        #     else:
        #         ans= (path(x+1,y)+path(x,y+1))
        #         d[(x,y)]=ans
        #         return ans
        # return path(0,0)