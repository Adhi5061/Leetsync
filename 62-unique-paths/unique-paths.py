class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def dp(i,j):
            if((i,j) in memo):
                return memo[(i,j)]
            if(i==0 and j==0):
                return 1
            if(i<0 or j<0):
                return 0
            ans=dp(i-1,j)+dp(i,j-1)
            memo[(i,j)]=ans
            return ans
        return dp(m-1,n-1)