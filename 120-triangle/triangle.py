class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        grid=triangle
        dp=[[0]* len(triangle[i]) for i in range(len(triangle))]
        dp[0][0]=triangle[0][0]
        for i in range(1,len(grid)):
            for j in range(0,len(grid[i])):
                if(j==0):
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                elif(j==len(triangle[i])-1):
                    dp[i][j]=grid[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        # print(dp)
        return min(dp[-1])
        
        
        # table=[[10**5] *len(triangle) for _ in range(len(triangle))]
        # table[0][0]=triangle[0][0]
        # for i in range(0,len(triangle)-1):
        #     for j in range(0,len(triangle[i])):
        #         table[i+1][j]=min(table[i+1][j],triangle[i+1][j]+table[i][j])
        #         table[i+1][j+1]=min(table[i+1][j+1],table[i][j]+triangle[i+1][j+1])
        # # print()
        # return min(table[-1])
        # memo={}
        # def dp(i,j):
        #     if((i,j) in memo):
        #         return memo[(i,j)]
        #     if(i==len(triangle) or j>=len(triangle[i])):
        #         return 0
        #     ans=triangle[i][j]+min(dp(i+1,j),dp(i+1,j+1))
        #     memo[(i,j)]=ans
        #     return ans  

        # return dp(0,0)