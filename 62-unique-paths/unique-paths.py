class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        table=[[0]*n]*m
        table[0]=[1]*len(table[0])
        for i in range(len(table)):
            table[i][0]=1
        for i in range(1,len(table)):
            for j in range(1,len(table[0])):
                table[i][j]=table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]
        

        # d={}
        # def dp(m,n):
        #     if (m,n) in d:
        #         return d[(m,n)]
        #     if(m<1 or n<1):
        #         return 0
        #     if(m==1 and n==1):
        #         return 1
        #     ans=dp(m-1,n)+dp(m,n-1)
        #     d[(m,n)]=ans
        #     return ans
        # return dp(m,n)