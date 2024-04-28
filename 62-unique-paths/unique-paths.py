class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        def dp(m,n):
            if (m,n) in d:
                return d[(m,n)]
            if(m<1 or n<1):
                return 0
            if(m==1 and n==1):
                return 1
            ans=dp(m-1,n)+dp(m,n-1)
            d[(m,n)]=ans
            return ans
        return dp(m,n)