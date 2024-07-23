class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(0,len(obstacleGrid)):
            for j in range(0,len(obstacleGrid[0])):
                if(obstacleGrid[i][j]==1):
                    dp[i][j]=0
                elif(i==0):
                    if(j>0 and dp[i][j-1]==0):
                        dp[i][j]=0
                    else:
                        dp[i][j]=1
                elif(j==0):
                    if(i>0 and dp[i-1][j]==0):
                       dp[i][j]=0
                    else:
                        dp[i][j]=1
                elif(obstacleGrid[i][j]==1):
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                # if(j==2):
                #     print(dp)
        # print(dp)
        return dp[-1][-1]
        # table=[[0]*len(obstacleGrid[0])]*len(obstacleGrid)
        # table[0][0]=1
        # for i in range(0,len(obstacleGrid)-1):
        #     for j in range(0,len(obstacleGrid[0])-1):
        #         if(obstacleGrid[i+1][j]==1 or obstacleGrid[i][j+1]==1):
                    
        #             continue
        #         table[i+1][j]=table[i+1][j]+table[i][j]
        #         table[i][j+1]=table[i][j+1]+table[i][j]
        # print(table)
        # return table[-1][-1]
        # row=len(obstacleGrid)
        # col=len(obstacleGrid[0])

        # memo={}
        # def dp(i,j):
        #     if((i,j) in memo):
        #         return memo[(i,j)]
        #     if(i==row-1 and j==col-1 and obstacleGrid[i][j]!=1):
        #         memo[(i,j)]=1
        #         return 1
        #     if(i>=row or j>=col):
        #         memo[(i,j)]=0
        #         return 0
        #     if(obstacleGrid[i][j]==1):
        #         memo[(i,j)]=0
        #         return 0
        #     ans=dp(i+1,j)+dp(i,j+1)
        #     memo[(i,j)]=ans
        #     return ans
        # return dp(0,0)


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