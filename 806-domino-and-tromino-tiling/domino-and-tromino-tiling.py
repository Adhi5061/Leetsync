class Solution:
    def __init__(self):
        self.memo={}
    def numTilings(self, n: int) -> int:
        if(n in self.memo):
            return self.memo[n]
        if(n<0):
            return 0
        if(n==0):
            return 1
        ans=self.numTilings(n-1)+self.numTilings(n-2)
        temp=0
        for i in range(3,n+1):
            temp+=self.numTilings(n-i)
            temp+=self.numTilings(n-i)
        self.memo[n]=temp+ans
        return (temp+ans)%((10**9)+7)