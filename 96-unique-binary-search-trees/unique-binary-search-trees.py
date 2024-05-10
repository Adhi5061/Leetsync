class Solution:
    def numTrees(self, n: int) -> int:
        
        memo={}
        def dp(n):
            if(n in memo):
                return memo[n]
            if(n==0):
                return 1
            # if(n==3):
            #     return 5
            res=0
            for i in range(1,n+1):
                left=dp(i-1)
                right=dp(n-i)
                res+=(left*right)
            memo[n]=res
            return res
        return dp(n)            

            