class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[0]*n for i in range(m)]
        # dp[0][0]=1
        # temp=[1]*n
        dp=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if(i<1 or j<1):
                    temp[j]=1
                    continue
                temp[j]=temp[j-1]+dp[j]
            dp=temp
        # print(dp)
        return dp[n-1]
        # memo={}
        # def dp(i,j):
        #     if((i,j) in memo):
        #         return memo[(i,j)]
        #     if(i==0 and j==0):
        #         return 1
        #     if(i<0 or j<0):
        #         return 0
        #     ans=dp(i-1,j)+dp(i,j-1)
        #     memo[(i,j)]=ans
        #     return ans
        # return dp(m-1,n-1)