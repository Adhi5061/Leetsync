class Solution:
    def numTilings(self, n: int) -> int:
        memo={}
        def rec(n):
            if(n in memo):
                return memo[n]
            if(n<0):
                return 0
            if(n==0):
                return 1
            ans=rec(n-1)+rec(n-2)
            temp=0
            for i in range(3,n+1):
                temp+=rec(n-i)
            temp+=temp
            memo[n]=(temp+ans)
            return (temp+ans)
        return rec(n)%((10**9)+7)