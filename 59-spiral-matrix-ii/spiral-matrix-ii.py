class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=t=0
        b=n-1
        r=n-1
        res = [[0 for _ in range(n)] for _ in range(n)]
        val=1
        while(l<=r and t<=b):
            i=l
            j=t
            while(i<=r):
                res[j][i]=val
                val+=1
                i+=1
            i-=1
            t+=1
            j=t
            while(j<=b):
                res[j][i]=val
                val+=1
                j+=1
            j-=1
            r-=1
            i=r
            while(i>=l and t<=b):
                res[j][i]=val
                val+=1
                i-=1
            i+=1
            b-=1
            j=b
            while(j>=t and l<=r):
                res[j][i]=val
                val+=1
                j-=1
            j+=1
            l+=1
        return res